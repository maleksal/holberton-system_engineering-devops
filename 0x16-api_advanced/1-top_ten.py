#!/usr/bin/python3
"""
Advanced API module

"""
import requests


def top_ten(subreddit):
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
    if request_info.status_code == 404:
        print(None)
    hottest = request_info.json().get("data").get("children")
    [print(child.get("data").get("title")) for child in hottest]


if __name__ == "__main__":
    number_of_subscribers()
