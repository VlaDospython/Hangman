def open_file(file):
    with open("words.txt", encoding="utf-8", ) as file:
        pass


if __name__ == '__main__':
    letter = input_normal_letter()
    print(f"Ви ввели букву: {letter}")
