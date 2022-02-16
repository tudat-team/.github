import jinja2
import time
import requests
import json
import os
import html
from sfn import get_news_articles, get_blogs, get_reports
from ll2 import get_launches
from gh import GitHub

BASE_TIME_URL = "https://www.timeanddate.com/worldclock/fixedtime.html?iso={iso}"
CACHE_DIR = "../cache"

# create cache dir if it doesnt exist
os.makedirs(CACHE_DIR, exist_ok=True)


def make_time_and_date_link(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    iso = time.strftime("%Y%m%dT%H%M%S", timestamp)
    return BASE_TIME_URL.format(iso=iso)


def make_datetime_human_readable(timestamp):
    """
    make a timestamp human readable
    """
    # get the timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC", timestamp)
    # timestamp = time.strftime("%B %d, %Y UTC", timestamp)
    return timestamp


def iso_datetime_string_to_datetime(s, milliseconds=True):
    if milliseconds:
        return time.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        return time.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def make_markdown_linked_time(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    s = make_datetime_human_readable(timestamp)
    url = make_time_and_date_link(timestamp)
    return f"[{s}]({url})"


def make_html_linked_time(timestamp):
    """
    create a link to a time and date
    """
    # convert the timestamp to a string in iso format
    s = make_datetime_human_readable(timestamp)
    url = make_time_and_date_link(timestamp)
    return f'<a href="{url}">{s}</a>'


from utils import download_file

import re


def get_build_status():
    ret = {}
    for feedstock in [
        ("sofa-cmake-feedstock", "master"),
        ("cspice-cmake-feedstock", "master"),
        ("nrlmsise-00-feedstock", "main"),
        ("tudat-resources-feedstock", "master"),
        ("tudat-feedstock", "master"),
        ("tudatpy-feedstock", "master")
    ]:

        # download readme
        url = f"https://raw.githubusercontent.com/tudat-team/{feedstock[0]}/{feedstock[1]}/README.md"
        download_file(url, f"{CACHE_DIR}/{feedstock[0]}.md", cache_dir=CACHE_DIR)

        # compile regex with multiple lines
        regex = r"(<table[^>]*>(?:.|\n)*<\/table>)"

        # regex all group between <table> and </table>
        with open(f"{CACHE_DIR}/{feedstock[0]}.md", "r") as f:

            # get the table
            s_file = f.read()
            matches = list(re.finditer(regex, s_file, re.MULTILINE))
            s_match = matches[0].group(1)

            # remove first occurrence of <table>
            s_match = s_match.replace("<table>", "", 1)

            # remove final occurrence of </table>
            s_match = "".join(s_match.rsplit("</table>", 1))

            s_match = s_match.replace("Azure", f"<code>{feedstock[0]}</code>")
            ret[feedstock[0]] = s_match

    return ret


# get readme data
def get_readme_data():
    """
    get the readme data for the readme file generation
    """
    # get build status
    build_status = get_build_status()

    # for space feed
    news_articles = get_news_articles(cache_dir=CACHE_DIR,
                                      cache_time=3600 // 2)

    blogs = get_blogs(cache_dir=CACHE_DIR,
                      cache_time=3600 // 2)

    return {
        "timestamp": time.gmtime(),
        "make_html_linked_time": make_html_linked_time,
        "news_articles": news_articles,
        "blogs": blogs,
        "build_status": build_status,
        "iso_datetime_string_to_datetime": iso_datetime_string_to_datetime
    }


if __name__ == "__main__":
    # load template file
    template_loader = jinja2.FileSystemLoader(searchpath="./templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("README.md.j2")

    # # # load data
    data = get_readme_data()

    # render template
    output = template.render(**data)

    # write output
    with open(os.path.join("..", "README.md"), "w") as f:
        f.write(output)
