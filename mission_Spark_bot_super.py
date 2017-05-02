from flask import Flask, request
import requests
import json

# Global variables
baseurl = "https://api.ciscospark.com/v1"

bot_auth_token = "NzJkMzE0ZjMtOWJjZS00Y2JkLWIyZjAtNDI4MjA0MjA0ZWIxNDgxNjY4NjMtZTlk"

headers = {"Content-Type": "application/json",
           "accept": "application/json",
           "Authorization": "Bearer %s" % bot_auth_token
           }

app = Flask(__name__)


def get_message(data):
    mess_id = data['id']

    #Python has powerful string and text manipulation.  
    # I recommend checking out https://learnpythonthehardway.org/book/ex6.html
    # for more info on this.
    mess_api = "/messages/%s" % mess_id

    mess_url = baseurl + mess_api

    mess_resp = requests.get(url=mess_url, headers=headers)

    mess_content = mess_resp.json()['text']  #This is not going to work, it is not a dictionary you can call a key on... yet

    mess_room = mess_resp.json()['roomId']   #Same thing here as the variable above

    return mess_room, mess_content  #In python you can return multiple return items in a function and unpack to multiple variables


def send_message(room, text):
    send_api = "/messages"

    send_url = baseurl + send_api

    send_data = {"roomId": room,
                 "text": text
                 }

    send_resp = requests.post(send_url,
                              headers=headers,
                              json=send_data)

    return send_resp


def get_membership(room, email):
    get_mem_api = "/memberships"

    get_mem_param = {"roomId": room,
                     "personEmail": email  # make sure the correct variale is referenced in this function
                     }

    get_mem_url = baseurl+get_mem_api  #some thing is missing...

    get_mem_resp = requests.get(url=get_mem_url,
                                params=get_mem_param,
                                headers=headers)

    print(get_mem_resp)

    # This conditional flow "if something is True... do something... else, do something different"
    # helps us control what happend next in our app / script.
    # "or" statements say only one of my true false definitions need to be true.
    #"and" would tell us both statements need to be true
    if get_mem_resp.status_code != 200 or json.loads(get_mem_resp.text)["items"] == []:
        get_mem_id = None
        print("Did not get the right response, please check to make sure the e-mail is correct")

    else:
        get_mem_id = json.loads(get_mem_resp.text)["items"][0]["id"]

    return get_mem_id


def rock_ban(mem_id):
    del_mem_api = "/memberships/%s" % mem_id

    ban_url = baseurl + del_mem_api

    ban_resp = requests.delete(url=ban_url, headers=headers)  #Looks reasonable, but something is not quite right...

    return ban_resp


@app.route('/ban/this/guy', methods=['POST'])
def ban_hook():
    spark_hook = request.get_json(silent=True)

    hook_data = spark_hook['data']

    mess_room, mess_content = get_message(hook_data)

    #The split function can split strings into variables
    #See simple tutorial on this here http://www.pythonforbeginners.com/dictionary/python-split
    #you can define what to split by inside the parentheses "some,text,is,neat".split(",")
    #if you leave it blank, like we did, it will split by a space.
    mess_list = mess_content.split()

    print(mess_list)

    #This conditional is looking for specific elements in the message
    # that was sent to the your bot.
    # If the message doesn't meet these criteria it will move to the else condition.
    # notice the statement mess_list[1] == "/ban": this is the main logic that we need to ban someone
    if hook_data['personEmail'] != "2manybots@sparkbot.io":
        if len(mess_list) >= 3 and mess_list[1] == "/ban" :

            mem_id = get_membership(mess_room, mess_list[2])
            print(mem_id)

            if mem_id is None:
                print("E-mail address not valid, user is not in this room!!!")

                print("We didn't end up banning anyone, DOH!")
                send = send_message(mess_room,
                                    "I can exile anyone, just say the word.  But they have to actually be in a room, and I have to be the moderator :-)")
                print(send)
            else:
                banned_for_life = rock_ban(mem_id)

                if banned_for_life.status_code == 204:
                    print("We banned that jerk %s" % mess_list[2])
                else:
                    print("I don't think we banned them, well this is embarrassing...")

                send = send_message(mess_room, "%s is now banned!!!!" % mess_list[2])

                print(send)
        else:
            print("We didn't end up banning anyone, DOH!")
            send = send_message(mess_room,
                                "I can exile anyone, just say the word.  But they have to actually be in a room, and I have to be the moderator :-)")
            print(send)

    return json.dumps({"did-it-work": "A-OK"})


if __name__ == '__main__':
    app.run(host="localhost", port=8080)