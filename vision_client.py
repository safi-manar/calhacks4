from google.cloud import vision
from google.cloud.vision import types

import gcp_credentials
import constants
import logger


def vision_labels(image_uuid):
    """
        image_uuid = The uuid name of an image stored on the GCP Storage.
    """


    # For internal debugging.

    # # The name of the image file to annotate
    # file_name = 'test.jpg'
    #
    # #Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()



    image_uri = "gs://{bucket_name}/{uuid}".format(bucket_name=constants.CLOUD_STORAGE_BUCKET, uuid=image_uuid)
    image_source = types.ImageSource(image_uri=image_uri)
    image = types.Image(source=image_source)

    # Performs label detection on the image file

    response = client.label_detection(image=image)
    labels = response.label_annotations

    labels_list = []
    for label in labels:
        labels_list.append(str(label.description))

    return labels_list


def _get_client():
    creds = gcp_credentials.get_credentials()
    client = vision.ImageAnnotatorClient(credentials=creds)
    return client


# Instantiates a client
client = _get_client()
