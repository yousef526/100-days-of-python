from flask import Flask, render_template
import random
import datetime as dt
import requests


app = Flask(__name__)

URL_gender = "https://api.genderize.io/"
URL_age = "https://api.agify.io/"



@app.route('/')
def home():
    value = random.randint(10,651)
    now = dt.datetime.now()

    return render_template("index.html",num=value,year_now=now.year)

@app.route('/guess/<string:name>')
def guess(name):
    age_ = requests.get(url=URL_age,params={"name":f"{name}"}).json()['age']

    gender_ = requests.get(url=URL_gender,params={"name":f"{name}"}).json()['gender']
    
    return render_template("guess.html",name_=name.capitalize(),age=age_,gender=gender_)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    
    data = response.json()
    return render_template("blog.html",paramter=data)

if __name__ == "__main__":
    app.run(debug=True)


