# ****************** The Model Layer

from flask import Flask, render_template
from model import db

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html', message = "Transmitting From The View Function", first_name="KURUKUTI", last_name="NARESH")

@app.route('/questions')
def questions_view():
    questions_db = db[0]
    return render_template("quiz.html", question=questions_db)

@app.route('/cool')
def cool():
    return "Flask is AWESOME!!!"

counter = 0

@app.route('/view_count')
def view_count():
    global counter
    counter +=1
    return f"This is page has been viewed {counter} times(s)"

if __name__=='__main__':
    app.run(debug=True)