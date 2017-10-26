import home
import json
from flask import jsonify
import uuid
import storage_client
import vision_client

db = home.db

class PhotoUnit(db.Model):
    labels = db.Column(db.String(120))
    trans_labels = db.Column(db.String(120))
    uuid = db.Column(db.String(120),  primary_key=True)

    def __init__(self, photo):
        self.uuid = str(uuid.uuid4())  # generate uuid
        self.upload_image(photo)
        self.labels = self.generate_labels()
        self.trans_labels = self.translate_labels()



    def __repr__(self):
        return '<PhotoUnit %r>' % self.id


    # Given a Base64 encoded image, upload it to the storage to be saved at self.uuid.
    def upload_image(self, image):
        storage_client.upload_image(image, self.uuid)

    # Generate the labels for the image stored at self.uuid, and return them as a string.
    def generate_labels(self):
        labels_list = vision_client.vision_labels(self.uuid)
        labels_list = labels_list[:3] # Grab only the first 3 labels.
        return json.dumps(labels_list)

    # Return the string labels in the format of a list.
    def get_labels(self):
        labels_string = self.labels
        return json.loads(labels_string)

    # Return a string representation of the translated labels list.
    def translate_labels(self):
        labels = self.get_labels()
        #  TODO   Translate the labels here using translate_client.
        return "[translated, labels]"

    # Return the translated labels in the format of a list.
    def get_trans_labels(self):
        trans_labels_string = self.trans_labels
        return json.loads(trans_labels_string)


    def to_json(self):
        return jsonify(source_string=self.source_string,
                       trans_string=self.trans_string,
                       uuid=self.uuid)