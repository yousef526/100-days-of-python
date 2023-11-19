from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    with app.app_context():
        db.create_all()
    return render_template(
        'index.html',
        books=db.session.query(Book).all(),
        cond = len(db.session.query(Book).all())
        )


@app.route("/add",methods=["POST","GET"])
def add():
    info = {}
    if request.method == "POST":
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    
    return render_template('add.html')


@app.route("/edit",methods=["POST","GET"])
def edit():
    
    id = int(request.args.get('params'))
    book = Book.query.get(id)

    if request.method == "POST":
        new_rate = request.form['rate']
        

        book.rating = float(new_rate)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html",book=book)

@app.route('/<num>')
def delete(num):

    id = int(num)
    book = Book.query.get(id)

    

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

