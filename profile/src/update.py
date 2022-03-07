import jinja2
import time
import requests
import json
import os
import html
from sfn import get_news_articles, get_blogs, get_reports
from ll2 import get_launches
from gh import GitHub
# from github import Github

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
import yaml
from bs4 import BeautifulSoup


def get_feedstock_build_status(which='stable'):
    ret = {}
    # open repositories.yml and load into dict
    with open("repositories.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    org_url = data["org_url"]
    repos = data["repositories"]
    for repo in repos:
        # download readme
        raw_url = org_url.replace("github.com", "raw.githubusercontent.com")
        feedstock_url = f"{org_url}/{repo['name']}-feedstock"
        feedstock_raw_url = f"{raw_url}/{repo['name']}-feedstock"
        repo_url = f"{org_url}/{repo['name']}"
        repo_raw_url = f"{raw_url}/{repo['name']}"

        readme_url = f"{feedstock_raw_url}/{repo['branches'][which]}/README.md"
        cached_readme_path = f"{CACHE_DIR}/{repo['name']}-{which}-feedstock.md"

        version_url = f"{repo_raw_url}/{repo['branches'][which]}/version"
        cached_version_path = f"{CACHE_DIR}/{repo['name']}-{which}-version"

        # download the readme to get build status generated from conda-smithy
        e1 = download_file(readme_url, cached_readme_path, CACHE_DIR)
        e2 = download_file(version_url, cached_version_path, CACHE_DIR)

        print(e1)
        print(e2)
        # get latest git tag version
        # r = requests.get(f"https://api.github.com/repos/tudat-team/{feedstock[0]}/tags")

        # compile regex with multiple lines
        regex = r"(<table[^>]*>(?:.|\n)*<\/table>)"

        # regex all group between <table> and </table>
        with open(cached_readme_path, "r") as f:
            # get the table
            s_file = f.read()
            matches = list(re.finditer(regex, s_file, re.MULTILINE))
            s_match = matches[0].group(1)

            # load into beautiful soup
            soup = BeautifulSoup(s_match, "html.parser")

            # get inside of table
            table = soup.table

            # find first level rows
            cells = table.tr.find_all("td", recursive=False)

            cell_build = cells[1]

        with open(cached_version_path, "r") as f:
            version = f.read().replace("\n", "")

        ret[repo['name']] = {'table': cells[1],
                             'version': version,
                             'repo_url': repo_url,
                             'feedstock_url': feedstock_url, }

    return ret


# get readme data
def get_readme_data():
    """
    get the readme data for the readme file generation
    """
    # get build status
    stable_build_status = get_feedstock_build_status(which='stable')
    unstable_build_status = get_feedstock_build_status(which='unstable')

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
        "stable_build_status": stable_build_status,
        "unstable_build_status": unstable_build_status,
        "iso_datetime_string_to_datetime": iso_datetime_string_to_datetime
    }


if __name__ == "__main__":
    # gh = Github(os.environ["GITHUB_TOKEN"])
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
