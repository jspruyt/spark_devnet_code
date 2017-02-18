import requests,uptime,datetime,json

ut = str(datetime.timedelta(seconds=uptime.uptime()))
body = {"roomId" : "Y2lzY29zcGFyazWYxODkzNjRkMGUx", "text" : ut}
headers = {
    "Authorization": "Bearer MzE2YmZiZDYmMwNWE2ZTMtNWU5",
    "Content-Type": "application/json"
    }
requests.request("POST", url="https://api.ciscospark.com/v1/messages",
    data=json.dumps(body), headers=headers)