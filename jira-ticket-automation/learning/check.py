# I'm using environment variables even when i am just learning and testing things out ....
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("ISSUE-URL")
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
        "summary": "just testing some things out 👍😂"}
})   

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)
data = json.loads(response.text)
print (data)