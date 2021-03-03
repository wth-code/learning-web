from flask import *
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://app1-ffc93.firebaseio.com/", None)


@app.route("/")
def home():
    results = firebase.get("/home", "")
    titles = []
    subtitles = []
    imgs = []
    links = []
    for i in results:
        titles.append(results[i]["title"])
        subtitles.append(results[i]["subtitle"])
        imgs.append(results[i]["img"])
        links.append(results[i]["link"])
    return render_template("index.html", title=titles, subtitle=subtitles, img=imgs, link=links)


@app.route("/school")
def school():
    return render_template("school.html")


@app.route("/edit/<link>")
def edit(link):
    try:
        detail = {}
        data = firebase.get("home", "")
        for i in data:
            if data[i]["link"] == link:
                detail = {"title": data[i]["title"],
                          "subtitle": data[i]["subtitle"],
                          "img": data[i]["img"],
                          "link": data[i]["link"],
                          "id": i}
        content = f'<div class="editor">{firebase.get("link", link)["content"]}</div>'
        return render_template("edit.html", content=Markup(content), detail=detail)
    except:
        return render_template("404.html")


@app.route("/<link>")
def details(link):
    try:
        detail = {}
        data = firebase.get("home", "")
        for i in data:
            if data[i]["link"] == link:
                detail = {"title": data[i]["title"],
                          "subtitle": data[i]["subtitle"],
                          "img": data[i]["img"],
                          "link": data[i]["link"],
                          "id": i}
        content = firebase.get("link", link)["content"]
        return render_template("thing.html", content=Markup(content), detail=detail)
    except:
        return render_template("404.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        title = request.form.get["title"]
        subtitle = request.form.get["subtitle"]
        link = request.form.get["link"]
        img = request.form.get["img"]
        if not title or not subtitle or not link or not img:
            flash("Something is empty")
        else:
            data = {"title": title,
                    "subtitle": subtitle,
                    "img": img,
                    "link": link}
            firebase.post("home", data)
            flash("Done !")
    else:
        return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
