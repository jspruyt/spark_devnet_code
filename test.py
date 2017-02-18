"""
Just a testing module
"""

from urllib.request import Request, urlopen
import json

def main():
    """
    main function
    """

    req = Request('https://api.ciscospark.com/v1/rooms?max=10')
    req.add_header('Authorization', \
        'Bearer MDhjYTcyYzktMjNhMC00NGVlLTg3NzQtZTNiMTYxODQzYjYyN2FhZWVjYjUtNGY4')

    response = urlopen(req)
    response_string = response.read().decode("utf-8")

    json_object = json.loads(response_string)

    print(json.dumps(json_object, sort_keys=True, indent=4))

    response.close()
    print('hello world!')



if __name__ == '__main__':
    main()
