"""
Just a testing module
"""

import requests
import json
import ciscosparkapi


def main():
    """
    main function
    """

    post_to_room()




def get_rooms():
    pass


def post_to_room():
    url = "https://api.ciscospark.com/v1/messages"
    access_token = "MDhjYTcyYzktMjNhMC00NGVlLTg3NzQtZTNiMTYxODQzYjYyN2FhZWVjYjUtNGY4"
    headers = {"Content-type" : "application/json; charset=utf-8", \
         "Authorization" : "Bearer " + access_token}
    markdown = ["**Warning!!!**", "*Warning!!!*", \
        "[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)"]


    for message in markdown:
        mdpayload = {"toPersonEmail": "adventure@sparkbot.io", "markdown": message}
        mdresponse = requests.post(url=url, json=mdpayload, headers=headers)

        print(mdresponse.status_code)
        print(mdresponse.text)


if __name__ == '__main__':
    main()
