import home
from flask import jsonify
import uuid

db = home.db

class PhotoUnit(db.Model):
    source_string = db.Column(db.String(120))
    trans_string = db.Column(db.String(120))
    uuid = db.Column(db.String(120),  primary_key=True)

    def __init__(self, source_string, trans_string, photo):
        self.source_string = source_string
        self.trans_string = trans_string
        # use the photo, upload to Google
        self.uuid = str(uuid.uuid4())   #generate uuid



    def __repr__(self):
        return '<PhotoUnit %r>' % self.id

    def to_json(self):
        return jsonify(source_string=self.source_string,
                       trans_string=self.trans_string,
                       uuid=self.uuid)