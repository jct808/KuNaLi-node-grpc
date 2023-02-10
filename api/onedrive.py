import webbrowser
from datetime import datetime
import json
import os
import msal

APP_ID = "ffca2600-a080-430a-ae1f-a509aaa3da60"
app_value = "RJE8Q~GOOA8qj3fyTnbfKT29m8TApQ2AdrB44bKk"
SCOPES = ['Files.ReadWrite']
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'


def generate_access_token(app_id, scopes):
    # Save Session Token as a token file
    access_token_cache = msal.SerializableTokenCache()

    # read the token file
    if os.path.exists('token/ms_graph_api_token.json'):
        access_token_cache.deserialize(open("token/ms_graph_api_token.json", "r").read())
        token_detail = json.load(open('token/ms_graph_api_token.json',))
        token_detail_key = list(token_detail['AccessToken'].keys())[0]
        token_expiration = datetime.fromtimestamp(int(token_detail['AccessToken'][token_detail_key]['expires_on']))
        if datetime.now() > token_expiration:
            os.remove('token/ms_graph_api_token.json')
            access_token_cache = msal.SerializableTokenCache()

    # assign a SerializableTokenCache object to the client instance
    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

    accounts = client.get_accounts()
    if accounts:
        # load the session
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else:
        # authetnicate your accoutn as usual
        flow = client.initiate_device_flow(scopes=scopes)
        print('user_code: ' + flow['user_code'])
        webbrowser.open('https://microsoft.com/devicelogin')
        token_response = client.acquire_token_by_device_flow(flow)

    with open('token/ms_graph_api_token.json', 'w') as _f:
        _f.write(access_token_cache.serialize())

    return token_response


def upload_file_to_one_drive(file_name):
    access_token = generate_access_token(APP_ID, SCOPES)
