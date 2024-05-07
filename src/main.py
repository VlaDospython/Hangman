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
import sys

if __name__ == '__main__':
    # які змінні нам треба
    list_of_all_player_letters = []
    computer_word = get_random_word()
    letter = input_normal_letter(list_of_all_player_letters)
    lives = 8
    player_word = len(computer_word) * ["_"]


    # код програми

    def check_letter():
        global letter, lives, player_word

        if str(letter) in str(computer_word):
            print("yesss")

            indexes = [i for i in range(len(computer_word)) if computer_word[i] == letter]

            list_player_word = list(player_word)

            for index in indexes:
                list_player_word[index] = letter

            player_word = ''.join(list_player_word)
        else:
            lives -= 1


    def func():
        global letter

        def func_():
            if computer_word == player_word:
                print(f'Ви відгадали слово: {computer_word}!')
                sys.exit(0)

            if lives == 0:
                print(f'Ви не відгадали слово: {computer_word}!')
                sys.exit(0)

            global letter
            letter = input_normal_letter(list_of_all_player_letters)
            func()

        print(f"Ви ввели букву: {letter}, computer_word: {computer_word}")
        check_letter()
        a = picture[lives].replace("$word", str("".join(player_word))).replace("$used", str(", ".join(list_of_all_player_letters)))
        print(a)
        func_()

    func()



