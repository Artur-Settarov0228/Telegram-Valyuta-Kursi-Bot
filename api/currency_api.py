import requests

URL = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"

CURRENCIES = ["USD", "EUR", "RUB", "GBP", "KZT", "TRY"]

def get_rates():
    try:
        response = requests.get(URL, timeout=5)
        data = response.json()

        rates = {}

        for item in data:
            if item["Ccy"] in CURRENCIES:
                rates[item["Ccy"]] = float(item["Rate"])

        return rates
    except:
        return None