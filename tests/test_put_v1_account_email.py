from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import Facade
from dm_api_account.generic.helpers.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = Facade(host='http://5.63.153.31:5051')
    login = "naruto_46"
    email = "naruto_46@mail.ru"
    password = "naruto_46_11"
    email_new = "naruto_461@mail.ru"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )

    json = ChangeEmail(
        login=login,
        password=password,
        email=email_new
    )
    response = api.account_api.put_v1_account_email(json=json)
