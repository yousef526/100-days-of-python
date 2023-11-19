from flask import Flask, render_template,redirect,url_for,request
import requests
import smtplib as smtp

app = Flask(__name__)

res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = res.json()

@app.route('/')
def index():
    return render_template('index.html',posts=data)


@app.route('/contact',methods=["GET"])
def contact():
    return render_template('contact.html',title="Contact Me")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/contact",methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    msg = request.form["message"]
    #print(name+" "+email+" "+" "+phone+" "+msg)
    with smtp.SMTP('smtp-mail.outlook.com',port=587) as connection: 
        connection.starttls()
        connection.login(email,password='Wtdbe6A92pU7Rm9')
        connection.sendmail(from_addr=email,
                            to_addrs='yousefalaa8190@gmail.com',
                            msg=f'subject:Welcome msg \n\n name{name}\n phone:{phone}\n msg:{msg}')
    return render_template('contact.html',title="Msg sent")



@app.route('/post/<num>')
def post(num):
    num = int(num)
    return render_template("post.html",target_post=data[num-1],img_number=num)

app.run(debug=True)