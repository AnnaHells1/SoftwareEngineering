def censor_text(sentence, forbidden_words):
    for word in forbidden_words:
        # Заменяем каждое вхождение слова независимо от регистра
        sentence = sentence.replace(word, '*' * len(word), -1)
    return sentence


def load_forbidden_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            forbidden_words = [word.strip().lower() for word in file.read().split()]
        return forbidden_words
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    sentence = input("Введите предложение: ")

    forbidden_words = load_forbidden_words('input.txt')

    if forbidden_words is not None:
        censored_sentence = censor_text(sentence.lower(), forbidden_words)
        print("Цензурированное предложение:")
        print(censored_sentence)
    else:
        print("Файл 'input.txt' не найден.")