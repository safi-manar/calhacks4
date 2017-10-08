import os



# General constants
DEBUG = bool(os.environ['DEBUG'])


# GCP Credentials
GCP_TYPE = os.environ["gcp_type"]
GCP_CLIENT_EMAIL = os.environ["gcp_client_email"]
GCP_PRIVATE_KEY = os.environ["gcp_private_key"]
GCP_PRIVATE_KEY_ID = os.environ["gcp_private_key_id"]
GCP_CLIENT_ID = os.environ["gcp_client_id"]
GCP_TOKEN_URI = os.environ["gcp_token_uri"]
# Other GCP Strings
GCP_SCOPE = 'https://www.googleapis.com/auth/cloud-platform'


# TODO Delete?
#vision_api_url="https://vision.googleapis.com/v1/images:annotate?key=" + os.environ['VISION_API_KEY']