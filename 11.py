from collections import Counter
import re

def count_words(text):
    # Используем регулярное выражение для разделения текста на слова
    words = re.findall(r'\b\w+\b', text.lower())

    # Считаем количество использований каждого слова
    word_counts = Counter(words)

    # Находим самое популярное слово и количество его использований
    most_common_word, count = word_counts.most_common(1)[0]

    return most_common_word, count

if __name__ == "__main__":
    # Задайте абсолютный путь к вашему файлу
    file_path = "C:/Пользователи/Анна/PycharmProjects/pythonProject/input.txt"

    try:
        # Читаем текст из файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        most_common_word, count = count_words(text)

        # Вывод результатов
        print(f"Самое популярное слово: {most_common_word}")
        print(f"Количество использований: {count}")

    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")