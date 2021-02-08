#python program does an epic currency conversion (really hard code) (definetly didnt go on stackoverflow every 2 seconds
#no more questions please bigman. thank you and just use it. now.

# Import requestie boi
import requests

#import the PHAT gui
import tkinter


#creating the epic gui nobody asked for
class


class Currency_convertor:
    # remove this and ill beat u
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # we are want base and rates yes so leave here ty
        self.rates = data["rates"]


        # comment look cool

    # amount with conversion because gangsta
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]


        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

    # main shablam


if __name__ == "__main__":
    print("Welcome to Currency Converter \n" )
    print("Here are all the country codes: https://fixer.io/symbols\n")
    print(Currency_convertor.rates)
    MY_ACCESS_KEY = "6b413894a1fc04d14cdf05ecc33d3fac"
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', MY_ACCESS_KEY)
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)
