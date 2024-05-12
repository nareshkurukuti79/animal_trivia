# ****************** Model - Template - View Pattern

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html', message = "Transmitting From The View Function", first_name="KURUKUTI", last_name="NARESH")

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