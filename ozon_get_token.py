import json
import os.path

import requests

# checking the “config.py” file with the client_id and client_secret parameters
if os.path.isfile("config.py"):
    from config import params

    cid = params.get("client_id")
    csecret = params.get("client_secret")
else:
    cid = input('Введите client_id: ')
    csecret = input('Введите client_secret: ')

url = "https://performance.ozon.ru/api/client/token"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
data = {
    "client_id": cid,
    "client_secret": csecret,
    "grant_type": "client_credentials"
}
response = requests.post(url, headers=headers, data=json.dumps(data))
token_data = response.json()
access_token = token_data.get("access_token")
expires_in = token_data.get("expires_in")
token_type = token_data.get("token_type")

print(f"Access Token: {access_token}")
print(f"Token Type: {token_type}")
print(f"Expires In: {expires_in} seconds")
