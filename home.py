import os
import sys
import json

import requests
import base64
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
home = Flask(__name__)
home.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(home)
from photo_unit import PhotoUnit
db.create_all()
db.session.commit()

@home.route('/', methods=['GET'])
def verify():
    return "Hello world", 200


@home.route('/api/v1/photo', methods=['POST'])
def add_photo():
    #
    photo = base64.decodestring(request.get_json()['photo'])
    # Do a bunch of google api calls here and then save to database.

    temp_unit = PhotoUnit("source string example", "translated string example", photo)
    db.session.add(temp_unit)
    # db.session.commit()
    return temp_unit.to_json()

@home.route('/api/v1/photo/<id>', methods=['DELETE'])
def delete_photo(id):
    PhotoUnit.query.filter(uuid=id).delete()
    db.session.commit()

@home.route('/api/v1/photo/<id>', methods=['GET'])
def get_photo_unit(id):
    """
    :param id:
    :return:
    """
    # Query database and return PhotoUnit object in JSON body.
    source = request.args.get('source')
    target = request.args.get('target')
    response = PhotoUnit.query.filter_by(uuid=id).first().get_translation_response(source, target)

    return response.to_json()


@home.route('/api/v1/photo/all', methods=['GET'])
def get_all_photo_units():
    return [x.to_json() for x in PhotoUnit.query.all()]