import os

vision_api_url="https://vision.googleapis.com/v1/images:annotate?key=" + os.environ['VISION_API_KEY']


DEBUG = bool(os.environ['DEBUG'])