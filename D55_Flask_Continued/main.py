from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<name>/<int:number>')
def greet(number, name):
    return f'<h1 style="text-align: center">Hello, {name}! You are {number} years old</h1>' \
           f'<p>Updated</p>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye_world1():
    return 'Bye, World!'


if __name__ == "__main__":
    app.run(debug=True)
