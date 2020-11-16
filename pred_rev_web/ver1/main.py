from flask import Flask, render_template
from forms import SubmitForm
app = Flask(__name__)

authors = ["Fredrik", "Kristoffer", "Teodor", "Joa97"]
app.config["SECRET_KEY"] = "94e7470803fe765d08320634c1659894"

@app.route('/')
@app.route('/home')
def home():
    form = SubmitForm()
    return render_template('home.html', title="Home", form=form)

@app.route('/about')
def about():
    return render_template('about.html',authors=authors, title="About")

if __name__ == "__main__":
    app.run(debug=True)