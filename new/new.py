'''Користувач вводить назву товару та його ціну, вивести назви товарів та їх ціну'''

import re

def for_name(text):
    k = input(text)
    while not bool(re.match(r'[A-Za-z]', k)):
        k = input(text)
    return str(k)
k = for_name('enter name: ')
name={str(i) for i in k.split()}


def for_price(message):
    n = input(message)
    while not bool(re.match(r"\d+", n)):
        n = input(message)
    return str(n)
n = for_price('enter price:')

price=[float(i) for i in n.split()]

prices=list(price)
names=list(name)
print(name)
print(price)

def total_price():
    a=0
    for price in prices:
        a+=price
    print(a)
total_price()

