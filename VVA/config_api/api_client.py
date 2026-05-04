import sys
from brapi import Brapi
import requests
from datetime import datetime

api_key = "8dXhmfw6c3yTHUhuaXLAd9"

client = Brapi(
    api_key=api_key,
)

if sys.version_info < (3,13):
    print("Use Python 3.13 para rodar este script.")
    exit()

def buscar_cotacaoAtual(tik):

    quote = client.quote.retrieve(tickers=tik)
    return quote.results[0].regular_market_price


def historico_tik(tick: str, periodo="1mo", intervalo="1d"):
    url = f"https://brapi.dev/api/quote/{tick}"

    params = {
        "range": periodo,
        "interval": intervalo,
        "token": tick
    }

    response = requests.get(url, params=params)
    data = response.json()

    dados = []

    if "results" not in data:
        return []

    for item in data["results"][0]["historicalDataPrice"]:
        dados.append({
            "data": datetime.fromtimestamp(item["date"]),
            "open": item["open"],
            "high": item["high"],
            "low": item["low"],
            "close": item["close"],
            "volume": item["volume"]
        })

    return dados


def dados_completos(tik):
    quote = client.quote.retrieve(tickers=tik)
    r = quote.results[0]

    return [{
        "open": getattr(r, "regular_market_open", None),
        "previousClose": getattr(r, "regular_market_previous_close", None),
        "volume": getattr(r, "regular_market_volume", None),
        "max": getattr(r, "regular_market_day_high", None),   
        "min": getattr(r, "regular_market_day_low", None),  
        "marketCap": getattr(r, "market_cap", None)
    }]



