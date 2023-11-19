from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello():
    return "hello world hello world"

@app.route('/about/')
def pr():
    return "prrp"

if __name__ == "__main__":
    app.run()