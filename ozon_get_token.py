import json
import os.path
import requests


class TokenGenerator:
    def __init__(self):
        if os.path.isfile("config.py"):
            # checking the “config.py” file with the client_id and client_secret parameters
            from config import params
            self.cid = params.get("client_id")
            self.csecret = params.get("client_secret")
        else:
            self.cid = input('Введите client_id: ')
            self.csecret = input('Введите client_secret: ')

    def generate_token(self):
        url = "https://performance.ozon.ru/api/client/token"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "client_id": self.cid,
            "client_secret": self.csecret,
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


token_sample = TokenGenerator()
token_sample.generate_token()
