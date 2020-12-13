import requests
import stored_data


def fetch_url(url: str):
    return requests.get(stored_data.base_url + url).text


def fetch_all():
    data = {
        "Poland": requests.get(stored_data.base_url).text,
        "Voivodeships": dict()
    }
    for v in stored_data.v_names.keys():
        data["Voivodeships"][v] = requests.get(stored_data.base_url + "wojewodztwo-" + v).text

    return data
