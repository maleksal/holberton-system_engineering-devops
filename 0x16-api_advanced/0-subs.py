#!/usr/bin/python3
"""
Advanced API module

"""
import requests


def number_of_subscribers(subreddit):
    """ Requests subscribers for a specific sub-reddit
    """
    main_url = "https://www.reddit.com"
    # set header
    headers = {
        "User-Agent": "Ubuntu:playing with API (by /u/Cyber)"}
    # get sub-reddit info
    get_subredd = requests.get(
        main_url + '/{}/about.json'.format(subreddit),
        allow_redirects=False,
        headers=headers)
    if get_subredd.status_code == 404:
        return 0
    return get_subredd.json().get("data").get("subscribers")


if __name__ == "__main__":
    number_of_subscribers()
