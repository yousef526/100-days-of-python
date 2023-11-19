from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")



@app.route('/login',methods=["POST"])
def login():
    if request.method == "POST":
        
        return render_template('login.html',name=request.form['username'],password=request.form['password'])
    else:
        return render_template("index.html")


app.run(debug=True)