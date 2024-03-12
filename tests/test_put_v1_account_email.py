import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "naruto_8"
    email = "naruto_8@mail.ru"
    password = "naruto_8_11"
    email_new = "naruto_81@mail.ru"
    json = {
        "login": login,
        "email": email,
        "password": password
    }
    json_new = {
        "login": login,
        "password": password,
        "email": email_new
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    time.sleep(2)
    response = api.account.put_v1_account_email(json=json_new)
