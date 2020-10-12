from flask import render_template, redirect, url_for, request
from app import app
from app.forms import BeamForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = BeamForm()
    if form.validate_on_submit():
        result = 23
        return render_template("index.html", form=form, result=result)
    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")