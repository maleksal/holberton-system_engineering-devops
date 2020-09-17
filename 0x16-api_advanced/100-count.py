#!/usr/bin/python3
"""
Advanced API module

"""
from collections import OrderedDict
import requests


def counter(letter, text):
    """ count letters
    """
    count = 0
    for i in text.split():
        if letter.lower() == i.lower():
            count += 1
    return count


def count_words(subreddit, word_list, dictionary={}, end=None, init=False):
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
        return print()
    try:
        hottest = request_info.json().get("data").get("children")

        for i in hottest:
            for e in word_list:
                if not init:
                    dictionary[e] = counter(e, i.get("data").get("title"))
                else:
                    len_ = dictionary[e] + counter(e, i.get("data").get("title"))
                    dictionary[e] = len_
        init = True
        # check for exit
        heckya = request_info.json().get("data").get("after")
        if not heckya:
            sorted_dict = OrderedDict(sorted(
                                        dictionary.items(),
                                        key=lambda x: x[1],
                                        reverse=True))
            if len(sorted_dict) != 0:
                for key, val in sorted_dict.items():
                    if val != 0:
                        print("{}: {}".format(key, val))
            else:
                print()
            return
        return count_words(subreddit, word_list, dictionary, heckya, init)
    except Exception:
        pass


if __name__ == "__main__":
    number_of_subscribers()
