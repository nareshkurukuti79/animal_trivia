

# 1 - Jinja (Creating templates)
# 2 - Werkzeug (http routing, map url's)

# installing flask
# pip install pipenv
# pipenv install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This is my very first flask app"

@app.route('/cool')
def cool():
    return "Flask is AWESOME!!!"

if __name__=='__main__':
    app.run(debug=True)