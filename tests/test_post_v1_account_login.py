from dm_api_account.models.login_credentials_model import LoginCredentialsModel
from dm_api_account.models.registration_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "naruto_14"
    email = "naruto_14@mail.ru"
    password = "naruto_14_11"
    json = RegistrationModel(
        login=login,
        email=email,
        password=password
    )
    json_login = LoginCredentialsModel(
        login=login,
        password=password,
        rememberMe=True
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    response = api.login.post_v1_account_login(json=json_login)
