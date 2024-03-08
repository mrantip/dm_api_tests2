from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "naruto_4",
        "email": "naruto_4@mail.ru",
        "password": "naruto_4_11"
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    print(token)
    print(response)
    print(response.json())
