# [START hello-app]
import os
from google.cloud import secretmanager
from flask import Flask

GOOGLE_CLOUD_PROJECT = "cloud-studio-369512"
# SECRET_NAME = os.getenv("SECRET_NAME")
SECRET_NAME="my-secret-value"
secret_client = secretmanager.SecretManagerServiceClient()

app = Flask('hello-cloudbuild')

def extract_secert(project_id, secret_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """
    version = "latest"
    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version}"

    # Access the secret version.
    response = secret_client.access_secret_version(request={"name": name})


    # Verify payload checksum.
    # crc32c = google_crc32c.Checksum()
    # crc32c.update(response.payload.data)
    # if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
    #     print("Data corruption detected.")
    #     return response

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    print("Plaintext: {}".format(payload))
    return payload


@app.route('/')
def hello():
    secret_value = extract_secert(GOOGLE_CLOUD_PROJECT,SECRET_NAME)
    greeting = f"Hello World! , this is {secret_value}"
    return greeting

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
# [END hello-app]
