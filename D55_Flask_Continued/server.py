from flask import Flask
from random import randint


app = Flask(__name__)


def header(function):
    def wrapper():
        return "<h1>" + function() + "<h1>"

    return wrapper

random_number = randint(1, 9)
# print(random_number) In case you want to check the random number!
@app.route('/')
@header
def hello_world():
    return "Guess a number between 0 and 9"


@app.route('/<int:number>')
def greet(number):
    if number < random_number:
        return "Too low" \
               "<br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return "Too high" \
               "<br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    else:
        return f"Bravo! You guessed {number}!"\
                "<br>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

@app.route('/bye')
def bye_world1():
    return 'Bye, World!'


if __name__ == "__main__":
    app.run(debug=True)
