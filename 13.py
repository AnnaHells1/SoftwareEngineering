def get_statistics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # Подсчет количества букв латинского алфавита
            alphabet_letters_count = sum(c.isalpha() and c.isascii() for c in text)

            # Подсчет количества слов
            word_count = len(text.split())

            # Подсчет количества строк
            line_count = text.count('\n') + 1

            return alphabet_letters_count, word_count, line_count
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'input.txt'

    statistics = get_statistics(file_path)

    if statistics is not None:
        alphabet_letters_count, word_count, line_count = statistics
        print(f"Количество букв латинского алфавита: {alphabet_letters_count}")
        print(f"Количество слов: {word_count}")
        print(f"Количество строк: {line_count}")
    else:
        print(f"Файл '{file_path}' не найден.")