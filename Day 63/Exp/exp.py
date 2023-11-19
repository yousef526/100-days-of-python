""" import sqlite3

db = sqlite3.connect("Exp/books-collection.db")
cursor = db.cursor()
cursor.execute(
    "CREATE TABLE books(\
        id INTEGER PRIMARY KEY,\
        title varchar(250) NOT NULL UNIQUE,\
        author varchar(250) NOT NULL,\
        rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit() """


from flask import Flask
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

with app.app_context():
    
    #db.create_all()

    """ new_book1 = Book ( title="What a Potter 2222 ", author="Varuana Ajmani", rating=9.7)
    new_book2 = Book ( title="What a Potter 2 ", author="Varuana Ajmani", rating=9.7)
    new_book3 = Book ( title="What a Potter 20 ", author="Varuana Ajmani", rating=9.7)
    db.session.add(new_book1)
    db.session.add(new_book2)
    db.session.add(new_book3)
    db.session.commit() """

    """ all_books = db.session.query(Book).all()
    print(all_books[0].title) """

    book = Book.query.filter_by(title="What a Potter 2222 ").first()
    print(book.id)