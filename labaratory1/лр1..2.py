print("Матвієнко Марія Едуардівна \nКМ-92\nЛабораторна робота 1,варіант 9 \n Підрахувати кількість цілих серед чисел а, b, с (ввеенні з клавіатури).")

a=float(input("введите первое число "))
b=float(input("введите второе число "))
c=float(input("введите третье число"))

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
















