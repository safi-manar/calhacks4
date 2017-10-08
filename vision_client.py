from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
import logger
import constants


def send_image(content):
    """
        content = a Base64 encoded image string
    """


    # For internal debugging.

    # # The name of the image file to annotate
    # file_name = 'test.jpg'
    #
    # #Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()


    image = types.Image(content=content)

    # Performs label detection on the image file

    response = client.label_detection(image=image)
    labels = response.label_annotations

    logger.log('Labels:')
    for label in labels:
        logger.log(label.description)

    return


def _get_client():
    keyfile_dict = _get_keyfile_dict()
    scope = [constants.GCP_SCOPE]
    creds = service_account.Credentials.from_service_account_info(keyfile_dict).with_scopes(scope)

    client = vision.ImageAnnotatorClient(credentials=creds)
    return client


def _get_keyfile_dict():
    keyfile_dict = {}
    keyfile_dict['type'] = constants.GCP_TYPE
    keyfile_dict['client_email'] = constants.GCP_CLIENT_EMAIL
    keyfile_dict['private_key'] = constants.GCP_PRIVATE_KEY
    keyfile_dict['private_key_id'] = constants.GCP_PRIVATE_KEY_ID
    keyfile_dict['client_id'] = constants.GCP_CLIENT_ID
    keyfile_dict['token_uri'] = constants.GCP_TOKEN_URI
    return keyfile_dict


# Instantiates a client
client = _get_client()
