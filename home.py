import os
import sys
import json

import requests
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

home = Flask(__name__)
home.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(home)


@home.route('/', methods=['GET'])
def verify():
    return "Hello world", 200






