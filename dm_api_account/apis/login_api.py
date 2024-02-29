class LoginApi:

    def __init__(self):
        ...

    def post_v1_account_login(self):
        """
        Authenticate via credentials
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/login"

        payload = {
            "login": "culpa labor",
            "password": "mollit tempor",
            "rememberMe": True
        }
        headers = {
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "POST",
            url,
            headers=headers,
            json=payload
        )
        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/login"

        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Accept': 'text/plain'
        }

        response = requests.request(
            method="DELETE",
            url=url,
            headers=headers
        )
        return response

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/login/all"

        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "DELETE",
            url,
            headers=headers
        )
        return response
