# Terminal Command Cheat Sheet: https://www.lemoda.net/windows/windows2unix/windows2unix.html

from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<strong>{text}</strong>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"
    return wrapper


# @app.route() -> Python Decorator
# ('/') -> specifies user is accessing the home/index page
@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p style="text-align:center"><em>How are you doing today?</em></p>'


@app.route("/bye")
@make_underline
@make_emphasis
@make_bold
def say_bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h3>Hello {name}, you are {number} years old!</h3>"


if __name__ == "__main__":
    app.run(debug=True)
