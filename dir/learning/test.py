import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("URL")
token = os.getenv("API_TOKEN")
mail = os.getenv("MAIL")

auth = HTTPBasicAuth(mail, token)
headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, auth=auth)
name = json.loads(response.text)
print(name[0]["name"])  