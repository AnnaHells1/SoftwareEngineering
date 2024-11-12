def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(content)
    except FileNotFoundError:
        print(f"Файл 'file_path' не найден")
    except Exception as e:
        print(f"Исключение: e")

if __name__ == '__main__':
    print("Для пустого файла:")
    read_file('input.txt')

    print("" + "=" * 30 + "")

    print("Для файла с информацией:")
    read_file('input.txt')