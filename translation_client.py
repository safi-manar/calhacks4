from google.cloud import translate
#import secret_env

import gcp_credentials

TRANSLATED_TEXT_LABEL = 'translatedText'

def translate_text(labels, source='en', target='en'):
    """
    :param labels: Either a str or a list of strings
    :param target:
    :return:
    """
    dicts = client.translate(labels, target_language=target, source_language=source)
    return [x[TRANSLATED_TEXT_LABEL] for x in dicts]


def _get_client():
    creds = gcp_credentials.get_credentials()
    client = translate.Client(credentials=creds)
    return client

client = _get_client()


def test():
    print(translate_text(['tomato', 'red'], target='es'))

