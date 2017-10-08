import home
from flask import jsonify

db = home.db

class PhotoUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_string = db.Column(db.String(120))
    trans_string = db.Column(db.String(120))
    photo = db.Column(db.LargeBinary)

    def __init__(self, source_string, trans_string, photo):
        self.source_string = source_string
        self.trans_string = trans_string
        self.photo = photo


    def __repr__(self):
        return '<PhotoUnit %r>' % self.id

    def to_json(self):
        return jsonify(id=self.id,
                       source_string=self.source_string,
                       trans_string=self.trans_string,
                       photo=self.photo)