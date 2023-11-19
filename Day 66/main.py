from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def dcit_to(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random',methods=["GET",])
def random_cafe_choose():
    data = 1212
    with app.app_context():
        data = db.session.query(Cafe).all()
        
    random_cafe = random.choice(data)
    return jsonify(cafe=random_cafe.dcit_to())

## HTTP GET - Read Record
@app.route('/all',methods=["GET",])
def all_cafe():

    with app.app_context():
        data = db.session.query(Cafe).all()
        
    """ cafes = []
    for ele in data:
        cafes.append(ele.dcit_to()) """
    return jsonify(cafe=[cafe.dcit_to() for cafe in data])

@app.route('/search',methods=["GET",])
def find_by_loc():
    title = request.args.get('loc')
    with app.app_context():
        data = Cafe.query.filter_by(location=title).first()
        
    if data:
        return jsonify(cafe=data.dcit_to())
    else:
        return jsonify(error={
        "NOT Found":"Sorry we don't have cafe at that location"    
        })


## HTTP POST - Create Record
@app.route('/add',methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        has_sockets = bool(request.form.get("sockets")),
        can_take_calls = bool(request.form.get("calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price")
    )

    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})




## HTTP PUT/PATCH - Update Record
@app.route('/update/<int:id>',methods=["POST"])
def update_coffe_price(id):
    new_cafe = Cafe.query.get(id)
    if new_cafe:
        new_cafe.coffee_price = request.args.get('new_price')
        with app.app_context():
            db.session.commit()

        return jsonify(response={"success": "Successfully updated the new coffe price."})
    else:
        return jsonify(error={"Not Found": "sorry cafe with that id not exist in the database"})
    

## HTTP DELETE - Delete Record
@app.route('/delete/<int:id>',methods=["GET"])
def delete_cafe(id):
    api_key = request.args.get('api-key')
    new_cafe = Cafe.query.get(id)
    if new_cafe and api_key == 'TopSecretAPIKEY':

        with app.app_context():
            db.session.delete(new_cafe)
            db.session.commit()

        return jsonify(response={"success": "Successfully updated the new coffe price."})
    else:
        return jsonify(error={"Not Found": "sorry cafe with that id not exist in the database"})

#"Peckham"
if __name__ == '__main__':
    app.run(debug=True)
