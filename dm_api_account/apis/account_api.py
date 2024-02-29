class AccountApi:
    def __init__(self):
        ...

    def post_v1_account(self):
        """
        Register new user
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account"

        payload = {
            "login": "naruto_2",
            "email": "naruto_2@mail.ru",
            "password": "naruto_2_11"
        }
        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
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

    def post_v1_account_password(self):
        """
        Reset registered user password
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/password"

        payload = {
            "login": "et aliquip esse",
            "email": "culpa Excepteur"
        }
        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
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

    def put_v1_account_email(self):
        """
        Change registered user email
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/email"

        payload = {
            "login": "eu dolor veniam labore",
            "password": "ut consequat dolore dolore",
            "email": "fugiat consequat aute"
        }
        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload
        )
        return response

    def put_v1_account_password(self):
        """
        Change registered user password
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account/password"

        payload = {
            "login": "eiusmo",
            "token": "urn:uuid:b822a57b-067b-9f63-59ad-0663a5e0486e",
            "oldPassword": "est consectetur",
            "newPassword": "officia aliquip id ut"
        }
        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Content-Type': 'application/json',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers,
            json=payload
        )
        return response

    def put_v1_account_token(self):
        """
        Activate registered user
        :return:
        """
        token = '123456789'
        url = f"http://5.63.153.31:5051/v1/account/{token}"

        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "PUT",
            url,
            headers=headers
        )
        return response

    def get_v1_account(self):
        """
        Get current user
        :return:
        """
        url = "http://5.63.153.31:5051/v1/account"

        headers = {
            'X-Dm-Auth-Token': 'aliquip labore in ipsum',
            'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
            'Accept': 'text/plain'
        }

        response = requests.request(
            "GET",
            url,
            headers=headers
        )
        return response
