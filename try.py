from firebase import firebase


firebase = firebase.FirebaseApplication("https://app1-ffc93.firebaseio.com/", None)

link = "js-firebase"

data = firebase.get("home", "")
for i in data:
    if data[i]["link"] == link:
        print(i)