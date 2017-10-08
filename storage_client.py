from google.cloud import storage
import gcp_credentials
import constants

def upload_image(image, uuid):
    bucket = client.get_bucket(constants.CLOUD_STORAGE_BUCKET)
    blob = bucket.blob(uuid)
    blob.upload_from_string(
        image,
        content_type=constants.CONTENT_TYPE
    )


def _get_client():
    creds = gcp_credentials.get_credentials()
    client = storage.Client(credentials=creds)
    return client


# Instantiates a client
client = _get_client()
