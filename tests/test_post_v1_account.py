from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "naruto_3",
        "email": "naruto_3@mail.ru",
        "password": "naruto_3_11"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)

