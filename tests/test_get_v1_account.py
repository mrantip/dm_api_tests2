from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "naruto_34"
    email = "naruto_3@mail.ru"
    password = "naruto_33_11"
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

    token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(headers=token)
    api.account.get_current_user_info()
