import home
from flask import jsonify

db = home.db

class PhotoUnit:
    id = db.Column(db.Integer, primary_key=True)
    source_string = db.Column(db.String(120))
    trans_string = db.Column(db.String(120))
    photo = db.Column(db.String(10000))

    def __init__(self, source_string, trans_string, photo):
        self.source_string = source_string
        self.trans_string = trans_string
        self.photo = photo


    def __repr__(self):
        return '<PhotoUnit %r>' % self.id

    def to_json(self):
        return jsonify(id=id,
                       source_string=source_string,
                       trans_string=trans_string,
                       photo=photo)