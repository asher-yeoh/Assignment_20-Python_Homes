from flask import Flask, jsonify, request
from flask_migrate import Migrate
from extensions import db
from models import Home
from schemas import HomeSchema
import csv

url = "postgres://postgres:postgres@localhost:5432/home_db"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

# http://127.0.0.1:5000/
@app.route("/")
def home():
    homes = Home.query.all()

    json_home = HomeSchema(many=True).dump(homes)

    return jsonify(json_home)

# http://127.0.0.1:5000/seed_homes
@app.route("/seed_homes")
def seed_homes():

    homes = []

    with open("homes.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
    
            home =  Home()

            home.sell = row["Sell"].replace(" ", "")
            home.list = row[" \"List\""].replace(" ", "")
            home.living = row[" \"Living\""].replace(" ", "")
            home.rooms = row[" \"Rooms\""].replace(" ", "")
            home.beds = row[" \"Beds\""].replace(" ", "")
            home.baths = row[" \"Baths\""].replace(" ", "")
            home.age = row[" \"Age\""].replace(" ", "")
            home.acres = float(row[" \"Acres\""].replace(" ", ""))
            home.taxes = row[" \"Taxes\""].replace(" ", "")
            
            db.session.add(home)
            db.session.commit()

            homes.append(home)

    json_home = HomeSchema(many=True).dump(homes)

    return jsonify(json_home)

# http://127.0.0.1:5000/create_home?sell=1&living=4
@app.route("/create_home")
def create_home():
    
    home =  Home()

    sell = request.args.get('sell')
    list = request.args.get('list')
    living = request.args.get('living')
    rooms = request.args.get('rooms')
    beds = request.args.get('beds')
    baths = request.args.get('baths')
    age = request.args.get('age')
    acres = request.args.get('acres')
    taxes = request.args.get('taxes')

    if sell is not None:
        home.sell = sell
    else:
        home.sell = 0

    home.list = list

    if list is not None:
        home.list = list
    else:
        home.list = 0
    
    if living is not None:
        home.living = living
    else: 
        home.living = 0
    
    if rooms is not None:
        home.rooms = rooms
    else:
        home.rooms = 0

    if beds is not None:
        home.beds = beds
    else:
        home.beds = 0

    if baths is not None:
        home.baths = baths
    else:
        home.baths = 0

    if age is not None:
        home.age = age
    else:
        home.age = 0

    if acres is not None:
        home.acres = acres
    else:
        home.acres = 0

    if taxes is not None:
        home.taxes = taxes
    else:
        home.taxes = 0

    db.session.add(home)
    db.session.commit()

    json_home = HomeSchema().dump(home)

    return jsonify(json_home)

# http://127.0.0.1:5000/home/6
@app.route("/home/<id>")
def displayHomeById(id):

    home = Home.query.get(id)
    json_home = HomeSchema().dump(home)

    return jsonify(json_home)

# http://127.0.0.1:5000/search_homes?max_age=30
# http://127.0.0.1:5000/search_homes?min_rooms=8
# http://127.0.0.1:5000/search_homes?min_beds=4
# http://127.0.0.1:5000/search_homes?min_baths=2
# http://127.0.0.1:5000/search_homes?max_age=30&min_rooms=8&min_beds=4&min_baths=2
@app.route("/search_homes")
def searchHomes():

    max_age = request.args.get("max_age")
    min_rooms = request.args.get("min_rooms")
    min_beds = request.args.get("min_beds")
    min_baths = request.args.get("min_baths")
    
    query = Home.query

    if max_age is not None:
        query = query.filter(Home.age <= max_age)
    if min_rooms is not None:
        query = query.filter(Home.rooms >= min_rooms)
    if min_beds is not None:
        query = query.filter(Home.beds >= min_beds)
    if min_baths is not None:
        query = query.filter(Home.baths >= min_baths)

    homes = query.all()
   
    json_home = HomeSchema(many=True).dump(homes)

    return jsonify(json_home)

# http://127.0.0.1:5000/search_homes/acres?min_acres=1.50&max_acres=4.0
@app.route("/search_homes/acres")
def searchHomesByAcres():

    min_acres = request.args.get("min_acres")
    max_acres = request.args.get("max_acres")
    
    query = Home.query

    query = query.filter(Home.acres >= min_acres, Home.acres <= max_acres)

    homes = query.all()
   
    json_home = HomeSchema(many=True).dump(homes)

    return jsonify(json_home)

app.run(debug=True)