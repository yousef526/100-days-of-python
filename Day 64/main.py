from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy,session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators
import requests
from sqlalchemy import exc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies.db"
Bootstrap(app)

db = SQLAlchemy(app)

API_KEY = "67d56a4d27d955f06edb5f304d531ed3"
TOKEN_ACCESS = """eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2N2Q1NmE0ZDI3ZDk1NWYwNmVkYjVmMzA0ZDUzMWVkMyIsInN1YiI6IjY1MjVhMjJkM2E0YTEyMDExZDIxY2JkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TIeT8Gd7cS1zr3RMaY41_yXihlplriqKi393Mv5fajk"""



class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description  = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


    
class rate_edit_change(FlaskForm):
    rating = StringField('rating', validators=[DataRequired()])
    review = StringField('your review', validators=[DataRequired(),])
    sumbit = SubmitField(label="Done")


@app.route("/",methods=["POST","GET"])
def home():
    all_moveis = movie.query.order_by(movie.rating).all()
    for i in range(len(all_moveis)):
        all_moveis[i].ranking = len(all_moveis) - i
    return render_template("index.html",movies=all_moveis)




@app.route("/delete",methods=["GET","POST"])
def delete():
    film = movie.query.get(int(request.args.get("params")))
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for("home"))


class movie_name(FlaskForm):
    movie_title = StringField(label="Movie title",validators=[DataRequired()])
    sumbit = SubmitField(label="Add a Movie")

movie_query = ""
url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "key":API_KEY,
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN_ACCESS}",
    
}


results = []
@app.route("/add",methods=["GET","POST"])
def add():
    form  = movie_name()
    if request.method == "POST":
        global movie_query
        movie_query = form.movie_title.data
        response = requests.get(
            url, headers=headers,params={"query":f"{movie_query}"}
        )
        global results
        results = response.json()['results']
        return render_template('select.html',results=results)
        

    return render_template("add.html",form=form)


@app.route("/find")
def add_new_movie():
    
    id_of_movie = request.args.get('movie')
    our_movie = {}

    for x in results:
        if id_of_movie == x['original_title'] :
            our_movie = x

    image_url = "https://image.tmdb.org/t/p/w500" + f"{our_movie['poster_path']}"
    new_movie = movie(
        title=our_movie['original_title'],
        year=our_movie['release_date'][:4],
        description=our_movie['overview'],
        img_url=image_url
    )


    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit',movie=new_movie.title))

@app.route("/edit",methods=["GET","POST"])
def edit():

    id = request.args.get("params")
    if id == None:
        id = request.args.get("movie")
    
    
    form = rate_edit_change()
    film = movie.query.filter_by(title=id).first()
    if form.validate_on_submit():
        
        film.rating = float(form.rating.data)
        film.review = form.review.data
        db.session.commit()
        all_moveis = db.session.query(movie).all()
        return render_template("index.html",movies=all_moveis)
    

    return render_template("edit.html",movie=film,form=form)


if __name__ == '__main__':
    app.run(debug=True)



"""new_movie = movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

 with app.app_context():
    db.create_all()
    db.session.add(new_movie)
    db.session.commit() """
