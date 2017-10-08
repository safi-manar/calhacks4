from google.cloud import vision
from google.cloud.vision import types
import io
import logger

# Instantiates a client
client = vision.ImageAnnotatorClient()


def send_image(content):
    """
        content = a Base64 encoded image string
    """


    # # The name of the image file to annotate
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'resources/wakeupcat.jpg')

    # Loads the image into memory
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
