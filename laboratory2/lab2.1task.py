'''Формула добутку'''
import re

def int_validator(message):
    n = input(message)
    while not bool(re.match(r'^\d+$', n)):
        n = input(message)
    return int(n)
n = int_validator('введіть n :')
x = int_validator('введіть x :')

p = 1
for i in range(1, n + 1):
    p = p * (x ** i + i)
print(p)
