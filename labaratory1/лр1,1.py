'''Вивести на екран символи, що дорівнюють кількісно номеру рядка '''

import re

a=input("введіть символ: ")
def int_validator(text):
    n = input(text)
    while not bool(re.match(r'^\d+$', n)):
        n = input(text)
    return int(n)
n=int_validator("кількість рядків: ")
i = 1
for i in range(n+1):
    print(a*i)








