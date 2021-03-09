# Needs pip for requests to be installed on the local machine
# you still need to install requests in pycharm
from requests import get
import tkinter


# GUI


class CurrencyConverter:

    rates = {}

    def __init__(self, web_url):
        data = get(web_url).json()

        # we want base rates
        self.rates = data["rates"]

    # amount with conversion
    def convert(self, from_currency, to_currency, money):
        initial_amount = money
        if from_currency != 'EUR':
            money = money / self.rates[from_currency]

        money = round(money * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, money, to_currency))

    # main


if __name__ == "__main__":
    print("Welcome to Currency Converter, please only enter currency titles in uppercase. (GBP, USD, TRY) \n")
    print("Here are all the country codes: https://fixer.io/symbols\n")
    MY_ACCESS_KEY = "6b413894a1fc04d14cdf05ecc33d3fac"
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', MY_ACCESS_KEY)
    c = CurrencyConverter(url)
    from_country = input("From Country: ")
    to_country = input("To Country: ")
    amount = int(input("Amount you'd like to convert: "))

    c.convert(from_country, to_country, amount)
