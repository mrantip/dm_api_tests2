from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "naruto_19"
    email = "naruto_19@mail.ru"
    password = "naruto_19_11"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    json_login = LoginCredentials(
        login=login,
        password=password,
        rememberMe=True
    )
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    response = api.login.post_v1_account_login(json=json_login)
    assert_that(response.resource, has_properties(
        {
            'login': login,
            'roles': [UserRole.guest, UserRole.player],
            'medium_picture_url': None
        }
    ))
