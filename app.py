from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import crud

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result = crud.read_courses()
    return render_template('home.html', result=result)

@app.route('/add',methods=['GET','POST'])
def index_add():
    result = crud.read_sheets()
    return render_template('index.html', result=result)

@app.route('/add/course', methods=['POST'])
def add():
    subject = request.form['subject']
    if subject == "Other":  
        subject = request.form['newsub']
        add_subject(subject)
    class_name = request.form['class']
    if class_name == "Other":
        class_name = request.form['newclass']
    assignment = request.form.getlist('assignments')
    weightage = request.form.getlist('weightages')
    # print(assignment)
    crud.add_course(subject, class_name, assignment, weightage)

    return redirect('/add')

# @app.route('/new/subject',methods=['GET','POST'])
# def new_subject():
#     result = crud.read_courses()
#     return render_template('home.html', result=result)

# @app.route('/new/subject/add',methods=['POST'])
# def new_subject_add():
#     result = crud.read_sheets()
#     subject = request.form['subject']
#     crud.add_subject(subject)

#     return redirect('/add')

if __name__ == '__main__':
    app.run(debug=True)
