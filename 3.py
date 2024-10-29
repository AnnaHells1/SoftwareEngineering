# Определяем базовый класс Car
class Car:
    # Конструктор класса Car
    def __init__(self, make, model):
        # Атрибуты класса
        self.make = make
        self.model = model

    # Метод для движения автомобиля
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Создаем подкласс ElectricCar, наследующий от Car
class ElectricCar(Car):
    # Конструктор класса ElectricCar
    def __init__(self, make, model, battery_capacity):
        # Вызываем конструктор родительского класса
        super().__init__(make, model)
        # Добавляем специфичный атрибут для электромобиля
        self.battery_capacity = battery_capacity

    # Метод для заряда батареи
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создаем экземпляр класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)

# Используем метод drive()
my_electric_car.drive()

# Используем метод charge()
my_electric_car.charge()