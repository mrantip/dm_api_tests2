from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "naruto_16"
    email = "naruto_16@mail.ru"
    password = "naruto_16_11"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
