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
    creds, keyfile_dict = gcp_credentials.get_credentials(with_keyfile=True)
    project = keyfile_dict['project_id']
    client = storage.Client(project=project, credentials=creds)
    return client


# Instantiates a client
client = _get_client()
