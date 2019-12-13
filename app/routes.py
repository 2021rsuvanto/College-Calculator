from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/collegecalculator', methods=["GET", "POST"])
def collegecalculator():
    user_input = dict(request.form)
    print(user_input)
    name = user_input["name"]
    school = user_input["school"]
    testtype = user_input["testtype"]
    score = int(user_input["score"])
    GPA = float(user_input["GPA"])
    print(name)
    print(school)
    print(testtype)
    print(score)
    print(GPA)
    print("Your dream school is " + school + ".")

    # output = model.scorecalculator(testtype, score, GPA, school)
    #
    # return render_template('results.html', name = name, GPA = GPA, output = output)
    # return "Keep at it!"
@app.route('/results')
def results():
        output = model.iterate(school, score, score, GPA, testtype)
        return output
        output2 = model.GPAAA(school, score, score, GPA, testtype)
        return output2
