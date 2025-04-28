from app import *
from flask import request


class User(db.Model):
    id = db.Column(db.integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

@app.before_first_request
def initialize_db() -> None:
    db.create_all()

@app.route("/", methods = ["GET"])
def generate_fake_data() -> None:
    name = fake.name()
    email = fake.unique_email()
    user = User(name = name, email = email)

    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201
