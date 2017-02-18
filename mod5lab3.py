"""
Just a testing module
"""
import requests


def main():
    """
    main function
    """
    # put the desired api call as the value
    url = "https://api.ciscospark.com/v1"
    api_call = '/people'

    # Provide your access token
    auth_token = "MDhjYTcyYzktMjNhMC00NGVlLTg3NzQtZTNiMTYxODQzYjYyN2FhZWVjYjUtNGY4"

    #Content type must be included in the header
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization" : "Bearer " + auth_token
    }

    # Parameter variable. The email belongs to a bot user, but we can use it for our code
    params = {"email":"sqtest-ciscospark-travisuser@squared.example.com"}

    url += api_call

    #Performs a GET on the specified api.
    response = requests.get(url, headers=headers, params=params).json()

    # print the json that is returned
    for item in response["items"]:
        print('Name: {}'.format(item['displayName']))
        print('email: {}'.format(item['emails'][0]))




if __name__ == '__main__':
    main()
