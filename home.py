import os
import sys
import json

import requests
from flask import Flask, request

home = Flask(__name__)


@home.route('/', methods=['GET'])
def verify():
    return "Hello world", 200
