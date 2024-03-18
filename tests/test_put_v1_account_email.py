import time

from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.registration_model import RegistrationModel
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
    login = "naruto_13"
    email = "naruto_13@mail.ru"
    password = "naruto_13_11"
    email_new = "naruto_131@mail.ru"
    json = RegistrationModel(
        login=login,
        email=email,
        password=password
    )
    json_new = ChangeEmailModel(
        login=login,
        password=password,
        email=email_new
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    time.sleep(2)
    response = api.account.put_v1_account_email(json=json_new)
