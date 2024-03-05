from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    # json = {
    #     "login": "naruto_2",
    #     "email": "naruto_2@mail.ru",
    #     "password": "naruto_2_11"
    # }
    token = 'a714e662-7c67-471d-bbf2-b9434e523ee6'
    # response = api.account.post_v1_account(
    #     json=json
    # )
    response_2 = api.account.put_v1_account_token(token=token)
    # print(response)
    print(response_2)




