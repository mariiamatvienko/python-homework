'''Підрахувати кількість цілих серед чисел а, b, с (ввеенні з клавіатури).'''

import re
def int_validator(message):
    n = input(message)
    while not bool(re.match(r'\d+', n)):
        n = input(message)
    return float(n)
a = int_validator('введите первое число:')
b = int_validator('введите второе число:')
c = int_validator('введите третье число:')

if float.is_integer(b) and float.is_integer(c) and float.is_integer(a):
  print("Цілих чисел-3")

elif float.is_integer(a) and float.is_integer(b):
         print("Цілих чисел-2")

elif float.is_integer(c) and float.is_integer(b):
        print("Цілих чисел-2")

elif float.is_integer(a) and float.is_integer(c):
        print("Цілих чисел-2")

else:
    if float.is_integer(a):
            print("Цілих чисел-1")
    if float.is_integer(b):
        print("Цілих чисел-1")
    if float.is_integer(c):
         print("Цілих чисел-1")
    if not float.is_integer(b) and not float.is_integer(c) and not float.is_integer(a):
        print("жодного цілого числа")
















