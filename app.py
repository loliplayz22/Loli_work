from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    email ="okoko26@nmhschool.org"
    number= "123-456-7890"
    is_faculty= True
    instagram = None
    return render_template("contact.html", email= email, is_faculty= is_faculty, number= number,instagram= instagram)


@app.route("/about")
def about():
    country = "Nigeria"
    is_senior=True
    return render_template("about.html", country= country, is_senior = is_senior)

app.run(debug=True)