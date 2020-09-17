#!/usr/bin/python3
"""
Advanced API module

"""
import requests


def recurse(subreddit, hot_list=[], end=None):
    """ prints the titles of the first 10 hot posts
    """

    main_url = "https://www.reddit.com"
    # set header
    headers = {
        "User-Agent": "Ubuntu:playing with API (by /u/Cyber)"}
    # get sub-reddit info
    request_info = requests.get(
        main_url + '/r/{}/hot.json?after={}'.format(subreddit, end),
        headers=headers,
        allow_redirects=False,
        )
    if request_info.status_code == 404:
        return None
    hottest = request_info.json().get("data").get("children")
    for i in hottest:
        hot_list.append(i.get("data").get("title"))
    heckya = request_info.json().get("data").get("after")
    if not heckya:
        return hot_list
    return recurse(subreddit, hot_list, heckya)


if __name__ == "__main__":
    number_of_subscribers()
