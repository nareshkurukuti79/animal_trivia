# ****************** Creating a REST API in Flask

from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html', 
                           questions=db)

@app.route('/questions/<int:index>')
def questions_view(index):
    try:
        questions_db = db[index]
        return render_template("quiz.html", 
                               question=questions_db, 
                               index=index, 
                               max_index=len(db)-1)
    except IndexError:
        abort(404)



@app.route('/cool')
def cool():
    return "Flask is AWESOME!!!"

counter = 0

@app.route('/view_count')
def view_count():
    global counter
    counter +=1
    return f"This is page has been viewed {counter} times(s)"


@app.route('/add_new_question', methods=['GET','POST'])
def add_question():
    if request.method=="POST":

        question_dict = {
            "question" : request.form['question'],
            "answer": request.form['answer']
        }
        db.append(question_dict)
        save_db()

        return redirect(url_for('questions_view', index=len(db) - 1))
    else:
        return render_template('add_questions.html')



#-----------------------------------------------------------------------------------
# Creating a REST API for Full-Stack Multi-Page App
@app.route('/api/questions/')
def api_question_list():
    return jsonify(db)

@app.route('/api/question/<int:index>')
def api_question_details(index):
    try:
        return jsonify(db[index])
    except IndexError:
        abort(404)


if __name__=='__main__':
    app.run(debug=True)