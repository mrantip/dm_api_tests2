import requests
import json


def post_v1_account():
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

response = post_v1_account()
print(response.request.url)
print(response.request.method)
print(response.request.headers)
print(response.request.body)

