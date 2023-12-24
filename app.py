from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key that is super secret you won't know"

#Create a Form Class



@app.route("/")
def index():
    first_name = "Shashank"
    stuff = 'This is <strong>Bold</strong>'
    return render_template("index.html", first_name=first_name, stuff=stuff)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404



if __name__ == "__main__":
    app.run(debug=True)

