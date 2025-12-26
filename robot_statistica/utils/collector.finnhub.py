import requests

def get_finnhub_data(symbol, api_key):
    url = "https://finnhub.io/api/v1/quote"
    r = requests.get(url, params={"symbol": symbol, "token": api_key}, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["c"], data["v"]

import requests

def get_polygon_data(symbol, api_key):
    url = f"https://api.polygon.io/v2/last/trade/{symbol}"
    r = requests.get(url, params={"apiKey": api_key}, timeout=10)
    r.raise_for_status()
    data = r.json()["results"]
    return data["p"], data["s"]
