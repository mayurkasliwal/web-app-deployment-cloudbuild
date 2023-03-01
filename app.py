# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START hello-app]
from flask import Flask
from google.cloud import secretmanager

GOOGLE_CLOUD_PROJECT = "cloud-studio-369512"
SECRET_NAME="my_secret_value"
client = secretmanager.SecretManagerServiceClient()

app = Flask('hello-cloudbuild')


@app.route('/')
def hello():
  client = secretmanager.SecretManagerServiceClient()
  name = f"projects/{GOOGLE_CLOUD_PROJECT}/secrets/{SECRET_NAME}/versions/latest"
  response = client.access_secret_version(name=name)
  payload = response.payload.data.decode("UTF-8")
  greeting = f"Hello everyone! , this is {payload}"
  return greeting

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
# [END hello-app]
