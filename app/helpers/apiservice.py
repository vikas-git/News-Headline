import requests

def get_api_data(url, payload):
    payload['apikey'] = '734987d9c01a4a79b04dcd30e44297bf'
    payload['limit'] = 10
    response = None
    try :
        response = requests.get(url, params=payload)
        response = response.json()

    except Exception as e:
        print(e)
    return response
