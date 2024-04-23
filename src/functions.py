from main import *
import random

def get_random_word():
    with open(encoding="utf-8", file="../res/words.txt", mode='r') as file:
        random_words = file.read().split()
        return random.choice(random_words)


def input_normal_letter():
    """
    - якщо користувач ввів символ не із українського алфавіту, то це "помилка"
    - якщо більше одного символа або 0 символів, то це "помилка"
    :return:
    > а
    > р
    > й
    > а
    """

    ukrainian_symbols_lower = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    player_letter = input("Введіть букву: ")
    if player_letter.lower() in ukrainian_symbols_lower and len(player_letter) == 1:
        if player_letter not in list_of_all_player_letters:
            list_of_all_player_letters.append(player_letter.lower())
            return player_letter.lower()
        else:
            print("Ви вже вводили таку саму букву, прохання ввести нову букву.")
            print()
            return input_normal_letter()
    else:
        print("Необхідно ввести одну українську букву.")
        print()
        return input_normal_letter()


if __name__ == '__main__':
    letter = input_normal_letter()
    print(f"Ви ввели букву: {letter}")
