from flask import Flask, render_template
import requests

app = Flask(__name__)


def guess_gender(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    data = response.json()
    gender = data["gender"]
    return gender


def guess_age(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    data = response.json()
    age = data["age"]
    return age


@app.route('/')
def home():
    return "<h1>Enter a name into the search bar above...</h1>"


@app.route('/guess/<name>')
def guess(name):
    gender = guess_gender(name)
    age = guess_age(name)
    return render_template("index.html", name=name, gender=gender, age=age)


@app.route('/blog')
def get_blog():
    response = requests.get(url="https://api.npoint.io/43471110d4bc5fd50218")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
