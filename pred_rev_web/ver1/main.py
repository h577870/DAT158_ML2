from flask import Flask, render_template, flash, redirect, url_for, request
from forms import SubmitForm
from options import Options
from formater import CustomFormatter
import sys
import random

app = Flask(__name__)

authors = ["Joakim Skålevik Høiby Hansen","Kristoffer Davidsen", "Teodor Alveberg", "Fredrik Christensen"]
app.config["SECRET_KEY"] = "94e7470803fe765d08320634c1659894"

def predict(form):
    #TODO: Kall metode som predikerer verdien, bruk form variablene for å sette features.
    form_formatted = CustomFormatter(form)
    print("Formatted form: ", form_formatted.string, file=sys.stdout)
    return random.randint(25, 19000)

@app.route("/",  methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = SubmitForm(request.form)
    options = Options()
    if request.form:
        if form.validate_on_submit():
            return render_template('home.html', title="Home", form=form, prediksjon=predict(form), options=options)
        else:
            return render_template('home.html', title="Home", form=form, invalid=True, options=options)
    return render_template('home.html', title="Home", form=form, options=options)

@app.route('/about')
def about():
    return render_template('about.html',authors=authors, title="About")

if __name__ == "__main__":
    app.run(debug=True)