import requests

def get_apify_limit(apify_key):

    url = "https://api.apify.com/v2/users/me/limits"

    bearer_string = "Bearer " + apify_key
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': bearer_string
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    return data["data"]["current"]["monthlyUsageUsd"]