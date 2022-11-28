from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<username>/<int:num>")
def hello_world(username=None, num=None):
    return render_template("index.html", name=username, num=num)


@app.route("/about.html")
def about():
    return render_template("about.html")
