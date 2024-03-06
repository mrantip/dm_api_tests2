import pprint

import requests


class MailhogApi:
    def __init__(self, host='http://5.63.153.31:5025', headers=None):
        self.host = host

    # self.account = AccountApi(host, headers)
    # self.login = LoginApi(host, headers)

    def get_api_v2_messages(self, limit=50):
        url = f"{self.host}/api/v2/messages?limit=50"

        response = requests.get(
            url=f"{self.host}/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def get_token_from_last_email(self):

response =MailhogApi().get_api_v2_messages(limit=50)
pprint.pprint(response.json())