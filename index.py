from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from webdav4.client import Client
import base64
import os
import time
import json
import sys
script_folder_path = os.path.dirname((os.path.realpath(__file__)))
sys.path.append(script_folder_path)

app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/uploadfile', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        URL = data["URL"]
        username = data["username"]
        password = data["password"]
        client = Client(URL, auth=(username, password))
        files = client.ls("/", detail=False)
        print(files)
        return json.dumps(files)
    else:
        return ""
        


if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888) #, ssl_context='adhoc'