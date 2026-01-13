from google.cloud import storage
import json

from google.cloud import storage

def load_all_documents(prefix: str = "") -> list:
    """
    Load all blobs from a GCS bucket as raw text.

    Args:
        prefix (str): Optional prefix to filter blobs by folder/path.

    Returns:
        List[str]: List of blob contents as plain text.
    """
    client = storage.Client()
    bucket = client.bucket("edb-hackathon-team12-bucket")
    documents = []

    for blob in bucket.list_blobs(prefix=prefix):
        text = blob.download_as_text()
        documents.append(text)

    return documents

