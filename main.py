from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
#from functions import get_user, get_order, get_offer
from classes_mosel import User, Offer, Order 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False

db = SQLAlchemy(app)



