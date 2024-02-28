import requests


def put_v1_account_token():
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
