from flask import Flask, render_template, flash, redirect, url_for, request
from forms import SubmitForm
from options import Options
from formater import CustomFormatter
import sys
import random
import pickle
import joblib
import numpy as np

app = Flask(__name__)

authors = ["Joakim Skålevik Høiby Hansen","Kristoffer Davidsen", "Teodor Alveberg", "Fredrik Christensen"]
app.config["SECRET_KEY"] = "94e7470803fe765d08320634c1659894"

model = joblib.load("../../finalized_model_17_nov.pkl")

def predict(form):
    form_formatted = CustomFormatter(form)
    return round(np.log(model.predict(form_formatted.df))[0], 2)

@app.route("/",  methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = SubmitForm(request.form)
    options = Options()
    if request.form:
        if form.validate_on_submit():
            return render_template('home.html', title="Home", form=SubmitForm(), prediksjon=predict(form), options=options)
        else:
            return render_template('home.html', title="Home", form=form, invalid=True, options=options)
    return render_template('home.html', title="Home", form=form, options=options)

@app.route('/about')
def about():
    return render_template('about.html',authors=authors, title="About")

if __name__ == "__main__":
    app.run(debug=True)