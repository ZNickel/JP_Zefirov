import random

import requests
import xml.etree.ElementTree as ET

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]


def get_response(yyyy: int, mm: int) -> str:
    d__format = "{:02d}/{:02d}/{:04d}".format(1, mm, yyyy)
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={d__format}"
    response = requests.get(url, headers={"User-Agent": random.choice(user_agents)})
    return response.text if response.status_code == 200 else response.status_code


def get_exchange_rate(currency_code: str, xml: str) -> float:
    root = ET.fromstring(xml)
    target_valute = None
    for valute in root.findall(".//Valute"):
        char_code = valute.find("CharCode").text
        if char_code == currency_code:
            target_valute = valute
            break
    if target_valute is None:
        return 1
    return float(target_valute.find("Value").text.replace(",", "."))


def get_rate_from_api(year: int, month_number: int, currency_code: str) -> float:
    xml = get_response(year, month_number)
    return get_exchange_rate(currency_code, xml)
