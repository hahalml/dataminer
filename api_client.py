import requests


def test_request(method, payload=None):

    r = requests.get('http://localhost:5000/{}'.format(method), params=payload)
    print(method, r.status_code,
          r.headers['content-type'],
          r.text)

if __name__ == "__main__":
    test_request("config")
    test_request("symbol_info", payload={"group": "NYSE"})
    test_request("symbols", payload={"symbol": "ETHBTC"})
    test_request("search", payload={"query": "eth", "type": "stock", "exchange": "NYSE", "limit": 5})
    test_request("history", payload={"symbol": "ethbtc", "from": 123, "to": 456, "resolution": "D"})
    test_request("marks", payload={"symbol": "ethbtc", "from": 123, "to": 456, "resolution": "D"})
    test_request("quotes", payload={"symbols": "NYSE%3AAA%2CNYSE%3AF%2CNasdaqNM%3AAAPL"})
