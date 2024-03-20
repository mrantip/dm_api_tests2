from ..models.login_credentials_model import LoginCredentials
from requests import Response, session
from restclient.restclient import RestClient


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials) -> Response:
        """
        Authenticate via credentials
        :param json login_credentials_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True)
        )
        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login",
        )
        return response

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login/all",
        )
        return response
