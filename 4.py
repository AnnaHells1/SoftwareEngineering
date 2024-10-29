class Car:
    def __init__(self, make, model):
        self.make = make  # Атрибут класса, хранящий марку автомобиля
        self.model = model  # Атрибут класса, хранящий модель автомобиля

    def drive(self):
        print(f"Driving the {self.make} {self.model}")  # Метод для вывода информации об автомобиле

# Создание экземпляра класса Car
myCar = Car("Toyota", "Corolla")  # Создаем объект Car с указанными параметрами

print(myCar.make)  # Выводит значение атрибута make объекта myCar
myCar.drive()  # Вызывает метод drive объекта myCar