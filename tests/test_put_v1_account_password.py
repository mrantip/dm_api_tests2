from services.dm_api_account import Facade
from dm_api_account.models import ChangePassword
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "naruto_43"
    email = "naruto_43@mail.ru"
    password = "naruto_43_11"
    oldPassword = password
    newPassword = "naruto_43_12"

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
    api.account.reset_registered_user_password(
        login=login,
        email=email
    )
    token = api.mailhog.get_token_for_reset_password(login=login)
    api.account.change_registered_user_password(login=login, token=token, old_password=oldPassword, new_password=newPassword)
