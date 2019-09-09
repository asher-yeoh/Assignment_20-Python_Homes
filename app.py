from flask import Flask, jsonify, request
from flask_migrate import Migrate
from extensions import db
from models import Home
from schemas import HomeSchema
import csv
import psycopg2

from collections import OrderedDict

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

app.run(debug=True)

# http://127.0.0.1:5000/create_home
@app.route("/create_home")
def create_home():

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

    homes = Home.query.all()

    json_home = HomeSchema(many=True).dump(homes)

    return jsonify(json_home)