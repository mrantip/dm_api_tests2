from ..models import *
from requests import Response
from restclient.restclient import RestClient
from dm_api_account.models.user_envelope_model import UserEnvelope
from ..utilities import validate_request_json


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: Registration, status_code: int = 201, **kwargs) -> Response:
        """
        Register new user
        :param status_code:
        :param json registration_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=validate_request_json(json),
            **kwargs
        )
        if status_code == 201:
            assert response.status_code == status_code, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
        return response

    def post_v1_account_password(self, json: ResetPassword) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json)
        )
        return response

    def put_v1_account_email(self, json: ChangeEmail) -> Response:
        """
        Change registered user email
        :param json change_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json)
        )
        return response

    def put_v1_account_password(self, json: ChangePassword) -> Response:
        """
        Change registered user password
        :param json change_password_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json)
        )
        return response

    def put_v1_account_token(self, token: str, status_code: int = 200, **kwargs) -> Response | UserEnvelope:
        """
        Activate registered user
        :param status_code:
        :param token
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(self) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
        )
        return response
