import time

# Определяем класс декоратора времени выполнения
class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  # Записываем время начала
        result = self.func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Записываем время окончания
        execution_time = end_time - start_time  # Подсчитываем время выполнения
        print(f"Время выполнения функции '{self.func.__name__}': {execution_time} секунд")  # Выводим время выполнения
        return result  # Возвращаем результат оригинальной функции

# Используем TimingDecorator для функции факториала
@TimingDecorator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Используем TimingDecorator для функции генерации квадратов
@TimingDecorator
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Основной блок выполнения
if __name__ == '__main__':
    print(factorial(5))  # Вычисляем и печатаем факториал числа 5
    print(generate_squares(5))  # Генерируем и печатаем квадраты чисел от 1 до 5