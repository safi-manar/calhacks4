import home
import json
from flask import jsonify
import uuid
import storage_client
import vision_client
import translation_client

db = home.db

class PhotoUnit(db.Model):
    labels = db.Column(db.Text)
    trans_labels = db.Column(db.Text)
    uuid = db.Column(db.String(40),  primary_key=True)

    def __init__(self, photo):
        self.uuid = str(uuid.uuid4())  # generate uuid
        self.upload_image(photo)
        self.labels = self.generate_labels()


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

    # Translation Methods

    # Given a target language, return a TranslationResponse object containing the source and target labels.
    #   If the target language does not already exist in the trans_labels dictionary, then translate_labels()
    #   will translate the labels via an API call and update the local state.
    def get_translation_response(self, source_lang, target_lang):
        target_labels = self.translate_labels(target_lang)
        source_labels = self.translate_labels(source_lang)
        response = TranslationResponse(source_labels, target_labels)
        return response

    # Main function for getting labels in a particular language.
    # Defaults to cached values, otherwise goes to Google
    def translate_labels(self, lang):
        trans_labels = self.get_trans_labels()
        # Labels are in english by default.
        if lang == 'en':
            return self.get_labels()
        # If translation already exists, use it.
        elif lang in trans_labels:
            return trans_labels[lang]
        else:
            # We have to generate this translation.
            return self.translate_new_labels(lang)

    # This should called when translation for target_lang has not been performed before.
    # Given a target language, update the local translation dictionary, and return a list of the labels translated
    #   in the target language.
    def translate_new_labels(self, target_lang):
        target_labels = translation_client.translate_text(self.get_labels(), target=target_lang)

        trans_labels = self.get_trans_labels()
        trans_labels[target_lang] = target_labels
        # Update the trans_labels
        self.trans_labels = json.dumps(trans_labels)

        return target_labels

    # Return the translated labels in the format of a dictionary, if it exists, elese an empty dictionary.
    def get_trans_labels(self):
        if self.trans_labels:
            # A dictionary already exists. Get it.
            trans_labels_string = self.trans_labels
            return json.loads(trans_labels_string)
        else:
            # No translation has been made yet. Return an empty dictionary.
            return {}


    def to_json(self):
        return jsonify(uuid=self.uuid)


class TranslationResponse:
    def __init__(self, source_labels, dest_labels):
        self.source_labels = source_labels
        self.dest_labels = dest_labels

    def to_json(self):
        return jsonify(source_labels=self.source_labels, dest_labels=self.dest_labels)
