from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import *
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app) ############## most import line to make boostrap work

class SignupForm(FlaskForm):
    username = StringField(label='Email',validators=[
        DataRequired(),
        validators.Email(message="Not valid email address"),
        ])
    password = PasswordField(label='Password',validators=[
        DataRequired(),
        validators.Length(min=8, message=('Field must be at least 8 characters')),
        ])
    submitField = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


email = 'admin@email.com'
password = "12345678"

@app.route("/login",methods=["POST","GET"])
def login():
    
    form = SignupForm(meta={'csrf':False})
    if form.validate_on_submit():
        if form.username.data == email and form.password.data == password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html',form=form)




if __name__ == '__main__':
    app.run(debug=True)