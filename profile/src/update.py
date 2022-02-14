import jinja2
import time
import requests
import json
import os
import html
import cv2
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


# get readme data
def get_readme_data():
    """
    get the readme data for the readme file generation
    """
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
