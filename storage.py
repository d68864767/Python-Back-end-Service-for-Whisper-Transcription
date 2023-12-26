```python
import os
import uuid
from google.cloud import storage

# Directory to store transcription files
TRANSCRIPTION_DIR = '/tmp/transcriptions'

# Google Cloud Storage bucket name
GCS_BUCKET_NAME = 'your-bucket-name'

def store_transcription(transcription_text):
    """
    Store a transcription in a text file and upload it to Google Cloud Storage.
    The transcription is given a unique ID which is returned.
    """
    # Ensure the transcription directory exists
    os.makedirs(TRANSCRIPTION_DIR, exist_ok=True)

    # Generate a unique ID for the transcription
    transcription_id = str(uuid.uuid4())

    # Save the transcription to a text file
    transcription_path = os.path.join(TRANSCRIPTION_DIR, '{}.txt'.format(transcription_id))
    with open(transcription_path, 'w') as f:
        f.write(transcription_text)

    # Upload the transcription file to Google Cloud Storage
    upload_to_gcs(transcription_path, '{}.txt'.format(transcription_id))

    return transcription_id

def retrieve_transcription(transcription_id):
    """
    Retrieve a transcription from Google Cloud Storage.
    If the transcription does not exist, return None.
    """
    # Download the transcription file from Google Cloud Storage
    transcription_path = download_from_gcs('{}.txt'.format(transcription_id))

    # If the transcription file does not exist, return None
    if transcription_path is None:
        return None

    # Read the transcription from the text file
    with open(transcription_path, 'r') as f:
        transcription_text = f.read()

    return transcription_text

def upload_to_gcs(local_path, gcs_path):
    """
    Upload a file to Google Cloud Storage.
    """
    client = storage.Client()
    bucket = client.get_bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path)

def download_from_gcs(gcs_path):
    """
    Download a file from Google Cloud Storage.
    If the file does not exist, return None.
    """
    client = storage.Client()
    bucket = client.get_bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(gcs_path)

    if not blob.exists():
        return None

    local_path = os.path.join(TRANSCRIPTION_DIR, gcs_path)
    blob.download_to_filename(local_path)

    return local_path
```
