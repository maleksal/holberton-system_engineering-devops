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
        main_url + '/r/{}/hot.json'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        )
    print(len(hot_list))
    if request_info.status_code == 404:
        return None
    hottest = request_info.json().get("data").get("children")
    for i in hottest:
        hot_list.append(i.get("data").get("title"))
        _end = i.get('data').get('after')
        if not _end:
            return hot_list
        return recurse(subreddit, hot_list, _end)
if __name__ == "__main__":
    number_of_subscribers()
