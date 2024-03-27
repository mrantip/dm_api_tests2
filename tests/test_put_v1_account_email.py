import time
from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "naruto_20"
    email = "naruto_20@mail.ru"
    password = "naruto_20_11"
    email_new = "naruto_201@mail.ru"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    json_new = ChangeEmail(
        login=login,
        password=password,
        email=email_new
    )
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    time.sleep(2)
    response = api.account.put_v1_account_email(json=json_new)
    assert_that(response.resource, has_properties(
        {
            'login': login,
            'roles': [UserRole.guest, UserRole.player],
            'status': None
        }
    ))
