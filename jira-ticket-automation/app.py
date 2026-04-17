from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
load_dotenv()

# flask app
app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create_ticket():
    url = os.getenv("ISSUE_URL")
    token = os.getenv("API_TOKEN")
    mail = os.getenv("MAIL")

    auth = HTTPBasicAuth(mail, token)
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    payload = json.dumps({
        "fields": {
            "project": {"key": "SCRUM"},      
            "issuetype": {"id": "10004"},       
            "summary": "CiCd pipeline has broken ... fix it "}
    })   

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",",":"))
app.run(host='0.0.0.0')