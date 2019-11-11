'''Обчислення конкретної функції, в залежності від введеного значення х'''

import math
import re

def int_validator(message):
    x = input(message)
    while not bool(re.match(r'^\d+$', x)):
        x = input(message)
    return float(x)

x = int_validator("enter x: ")

if x <= 1 and x >= 0:
    b = x ** 2 - x
    print("F(x)=", b)

else:
    if x > 1 or x < 0:
        print("F(x)=", x ** 2 - math.sin(math.pi * x ** 2))
