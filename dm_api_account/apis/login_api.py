import requests
from ..models.login_credentials_model import login_credentials_model
from requests import Response


class LoginApi:

    def __init__(self, host):
        self.host = host

    def post_v1_account_login(self, json: login_credentials_model) -> Response:
        """
        Authenticate via credentials
        :param json login_credentials_model
        :return:
        """

        response = requests.request(
            "POST",
            url=f"{self.host}/v1/account/login",
            json=json
        )
        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """

        response = requests.request(
            method="DELETE",
            url=f"{self.host}/v1/account/login",
        )
        return response

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """

        response = requests.request(
            "DELETE",
            url=f"{self.host}/v1/account/login/all",
        )
        return response
