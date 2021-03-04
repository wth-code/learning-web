from firebase import firebase


firebase = firebase.FirebaseApplication("https://app1-ffc93.firebaseio.com/", None)


data = firebase.get("home", "")
for i in data:
    firebase.put(f"home/{i}", "genre", "code")