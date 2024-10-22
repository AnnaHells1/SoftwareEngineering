def calculate_average_grade(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_students = len(lines)
            total_grades = sum(int(line.split(':')[1].strip()) for line in lines)

            if total_students > 0:
                average_grade = total_grades / total_students
                return average_grade
            else:
                return None
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = 'input.txt'

    average_grade = calculate_average_grade(file_path)

    if average_grade is not None:
        print(f"Средний балл всех студентов: {average_grade:.2f}")
    else:
        print(f"Файл '{file_path}' не найден или не содержит данных.")