from sys import argv
from datetime import date
from requests import get, utils

resp = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = resp.split("<Value ID=")
    d, m, y = map(int, content[0].split('"')[-4].split("."))

    for i in content:
        if code.upper() in i:
            print(date(year=y, month=m, day=d), end=', ')
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__main__":
    word = argv[1]
    print(currency_rates(word))
