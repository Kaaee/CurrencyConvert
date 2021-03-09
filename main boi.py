# Needs pip for requests to be installed on the local machine
# you still need to install requests in pycharm
import requests

# GUI Import
import tkinter


# GUI


class currency_converter:

    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # we want base rates
        self.rates = data["rates"]

    # amount with conversion
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

    # main




if __name__ == "__main__":
    print("Welcome to Currency Converter \n")
    print("Here are all the country codes: https://fixer.io/symbols\n")
    MY_ACCESS_KEY = "6b413894a1fc04d14cdf05ecc33d3fac"
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', MY_ACCESS_KEY)
    c = currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)
