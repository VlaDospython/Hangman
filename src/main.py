"""
Hangman – інструкція до гри.

У гравця є 8 життів. Кожен хід гравець намагається
вгадати 1 букву із загаданого слова:
 - якщо користувач пише букву, яка вже була введена, то це "помилка" і програма
   просить ввести букву ще раз
 - якщо буква є декілька разів у слові, то вона відображається на всіх місцях
 - якщо користувач ввів символ не із українського алфавіту, то це "помилка" ...
 - якщо більше одного символа або 0 символів, то це "помилка"
Життя зникає тільки тоді, коли введена нова буква із українського алфавіту, але її немає в слові.
Усі букви, які було введено повинні відображатися
"""
# абстрактний підхід до написання коду

from data import *
from functions import *

if __name__ == '__main__':
    # які змінні нам треба
    list_of_all_player_letters = []
    computer_word = get_random_word()
    letter = input_normal_letter(list_of_all_player_letters)
    lives = 8
    player_word = len(computer_word) * ["_"]

    # код програми

    def check_letter():
        print(letter)
        print(computer_word)
        for a in computer_word.split():
            if a == letter:
                print("djfdv")

        if letter in computer_word:
            return True
        else:
            return False


    def func():
        def func_():
            letter = input_normal_letter(list_of_all_player_letters)
            func()

        print(f"Ви ввели букву: {letter}")
        a = picture[lives].replace("$word", str("".join(player_word))).replace("$used", str(", ".join(list_of_all_player_letters)))
        print(a)
        func_()

    if check_letter():
        # for a in computer_word.split():
        #     if a == letter:
        #         a = letter
        #         print(computer_word)

        func()
    else:
        lives -= 1
        func()

