'''з'ясувати, чи існує цифра 2 у введеному числі'''
import re

def int_validator(message):
    n = input(message)
    while not bool(re.match(r'^\d+$', n)):
        n = input(message)
    return str(n)
n = int_validator("enter digit: ")

if "2" in n:
    print("number 2 exists")
else:
    print("number 2 does not exist")

