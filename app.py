from flask import Flask, jsonify, request
from flask_migrate import Migrate
from extensions import db
from models import Home
from schemas import HomeSchema

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