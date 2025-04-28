from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import os

# Importing and instantiating Flask
app = Flask(__name__)

DB_USER = os.getenv('MYSQL_USER', 'root')
DB_PASS = os.getenv('MYSQL_PASSWORD', 'password123')
DB_HOST = os.getenv('MYSQL_HOST', 'localhost')
DB_NAME = os.getenv('MYSQL_NAME', 'users')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuring connection with database
db = SQLAlchemy(app)

# Configuring and intantiating Faker for fake data
fake = Faker('pt_BR')

from app.routes import *
