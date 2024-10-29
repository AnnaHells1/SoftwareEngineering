# Определение класса Car
class Car:
    # Метод инициализации объекта класса
    def __init__(self, make, model):
        # Атрибуты класса
        self.make = make
        self.model = model

# Создание экземпляра класса
myCar = Car("Toyota", "Mazda")