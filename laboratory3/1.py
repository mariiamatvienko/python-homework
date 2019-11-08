def input_int(n):
    try:
        n = int(n)
    except ValueError:
        print('\nНевірний символ, спробуйте ще раз')
        n = input_int(input("\nОберіть n: "))
    if n <= 0:
        print("\nЗначення n не може бути від'ємним. Спробуйте ще раз")
        n = input_int(input("\nОберіть n: "))
    return n;

def main():
    n = input_int(input("Оберіть n: "))
    string = input("\nВведіть рядок: ")
    while string == "":
        print("\nВи ввели пустий рядок. Спробуйте ще раз!")
        string = input("\nВведіть рядок: ")
    print("\nВведений рядок: ", string)
    split_string = string.split();
    print("\nОкремі слова в рядку: ", split_string)
    new_string_list = list()
    for word in split_string:
        if len(word) < n:
            k = 0
            word_characters = list(word)
            for i in word_characters:
                if i == "a" or i =="а" or i == "а":
                    word_characters[k] = "d"
                k = k + 1
            new_word = "".join(word_characters)
            new_string_list.append(new_word)
        else:
            new_string_list.append(word)
    new_string = " ".join(new_string_list)
    print("\nРезультат: ", new_string)
    again = input("\nЩе раз? 1 - так, інше - ні")
    if again == "1":
        main()
    else:
        print("\nДо побачення! :)")
print("\nЛАБОРАТОРНА РОБОТА №3\nна тему: \"Рядки\"\nВиконала: Матвієнко М.Е.\nГрупа: КМ-92\n")
main()
