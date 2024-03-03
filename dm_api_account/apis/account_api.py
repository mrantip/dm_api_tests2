import requests
from ..models.registration_model import registration_model
from ..models.reset_password_model import reset_password_model
from ..models.change_email_model import change_email_model
from ..models.change_password_model import change_password_model
from requests import Response, session



class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers = headers

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        Register new user
        :param json registration_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: reset_password_model) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """

        response = requests.request(
            "POST",
            url=f"{self.host}/v1/account/password",
            json=json
        )
        return response

    def put_v1_account_email(self, json: change_email_model) -> Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """

        response = requests.request(
            "PUT",
            url=f"{self.host}/v1/account/email",
            json=json
        )
        return response

    def put_v1_account_password(self, json: change_password_model) -> Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """

        response = requests.request(
            "PUT",
            url=f"{self.host}/v1/account/password",
            json=json
        )
        return response

    def put_v1_account_token(self, token: str) -> Response:
        """
        Activate registered user
        :param token
        :return:
        """

        response = requests.request(
            "PUT",
            url=f"{self.host}/v1/account/{token}",
        )
        return response

    def get_v1_account(self) -> Response:
        """
        Get current user
        :return:
        """

        response = requests.request(
            "GET",
            url=f"{self.host}/v1/account",
        )
        return response
