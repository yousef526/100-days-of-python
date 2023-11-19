from flask import Flask, render_template
import requests

app = Flask(__name__)
res = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = res.json()
@app.route('/')
def home():
    
    return render_template("index.html",posts=data)

@app.route('/post/<num>')
def post(num):
    num = int(num)
    return render_template("post.html",target_post=data[num-1])

if __name__ == "__main__":
    app.run(debug=True)
