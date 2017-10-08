import os
import sys
import json

import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
home = Flask(__name__)
home.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(home)

from photo_unit import PhotoUnit

@home.route('/', methods=['GET'])
def verify():
    return "Hello world", 200


@home.route('/api/v1/photo', methods=['POST'])
def add_photo():
    #
    photo = request.json['photo']
    # Do a bunch of google api calls here and then save to database.
    temp_unit = PhotoUnit("source string example", "translated string example", "\x00\x26\x26")
    return temp_unit.to_json()

@home.route('/api/v1/photo/<int:id>', method=['DELETE'])
def delete_photo(id):
    PhotoUnit.query.filter(id=id).delete()
    db.session.commit()

@home.route('/api/v1/photo/<int:id>', methods=['GET'])
def get_photo_unit(id):
    # Query database and return PhotoUnit object in JSON body.
    return PhotoUnit.query.filter_by(id=id).first().to_json()



