# Определяем базовый класс Shape
class Shape:
    # Метод area() объявлен как абстрактный (пустой), 
    # так как мы не знаем, как вычислить площадь для всех фигур
    def area(self):
        pass

# Создаем подкласс Rectangle, наследующийся от Shape
class Rectangle(Shape):
    # Конструктор инициализирует ширину и высоту прямоугольника
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Переопределяем метод area() для прямоугольника
    def area(self):
        # Вычисляем площадь как произведение ширины и высоты
        return self.width * self.height

# Создаем подкласс Circle, наследующийся от Shape
class Circle(Shape):
    # Конструктор инициализирует радиус круга
    def __init__(self, radius):
        self.radius = radius

    # Переопределяем метод area() для круга
    def area(self):
        # Используем приближенное значение pi (3.14)
        # и формулу S = πr^2 для вычисления площади круга
        return 3.14 * self.radius * self.radius

# Создаем объект прямоугольника
myRectangle = Rectangle(20, 30)

# Вычисляем и выводим площадь прямоугольника
result1 = myRectangle.area()
print(result1)  # Выведет: 600

# Создаем объект круга
myCircle = Circle(20)
# Вычисляем и выводим площадь круга
result2 = myCircle.area()
print(result2)  # Выведет: 1256.0