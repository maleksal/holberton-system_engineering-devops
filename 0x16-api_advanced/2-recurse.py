#!/usr/bin/python3
"""
Advanced API module

"""
import requests


def recurse(subreddit, hot_list=[], counter=0):
    """ prints the titles of the first 10 hot posts
    """

    main_url = "https://www.reddit.com"
    # set header
    headers = {
        "User-Agent": "Ubuntu:playing with API (by /u/Cyber)"}
    # get sub-reddit info
    request_info = requests.get(
        main_url + '/r/{}/hot.json?limit=10'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        )
    if request_info.status_code == 404:
        return None
    hottest = request_info.json().get("data").get("children")
    if len(hot_list) == len(hottest):
        return hot_list
    hold_from_hottest = hottest[counter].get("data").get("title")
    hot_list.append(hold_from_hottest)
    counter += 1
    return recurse(subreddit, hot_list, counter)

if __name__ == "__main__":
    number_of_subscribers()
