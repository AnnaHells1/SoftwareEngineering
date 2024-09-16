# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнила:
- Кукурузняк А.Д.
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Выведите в консоль три строки. Первая – любое число. Вторая – любое число в виде строки. Третья – любое число с плавающей точкой.

```python
print(123)
print('321')
print(3.21)
```
### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/1.png)

## Выводы
С помощью print выводим строки в консоль. Чтобы вывести строчку - содержимое заносим в ковычки. 

## Лабораторная работа №2
### Выведите в консоль три строки. Первая – результат сложения или вычитания минимум двух переменных типа int. Вторая – результат сложения или вычитания минимум 
### двух переменных типа float. Третья – результат сложения или вычитания минимум двух переменных типа int и float.

```python
print(3249+4324)
print(6.2+93.3)
print(9 + 7.1 + 4.34 + 2)
```
### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/2.png)

## Выводы
С помощью print выводим строки в консоль.

## Лабораторная работа №3
###  Выведите в консоль три строки. Первая – обычная строка. Вторая – F строка с 
###  использованием заранее объявленной переменной. Третья – сложите две или более строк в 
###  одну.

```python
print('Привет, мир!')

world = 'Мир'
print(f'Привет, {world}!')

one = 'Привет, '
two = 'Мир!'
print(one + two)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/3.png)

## Выводы
Я научился выводить строки в консоль, а также научился пользоваться f-строкой. Изучил что такое конкатенация. 

## Лабораторная работа №4
###  Выведите в консоль три строки. Первая – трансформация любого типа переменной в bool. 
###  Вторая – трансформация любого типа переменной в float или int. Третья – трансформация 
###  любого типа переменной в str

```python
one = 'Hello'
print(bool(one))

two = 142
print(float(two))

three = None
print(str(three))
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/4.png)

## Выводы
Я изучил как приводить переменные к типам данных.

## Лабораторная работа №5
###  Присвойте трем переменным различные значения, воспользовавшись функцией input().

```python
one = input('one: ')
two = input('two: ')
three = input('three: ')
print(one, two, three)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/5.png)

## Выводы
Я научился пользоваться функцией консольного ввода input().

## Лабораторная работа №6
###  Создайте две любые числовые переменные и выполните над ними несколько математических 
###  операций: возведение в степень, обычное деление, целочисленное деление, нахождение 
###  остатка от деления. При желании вы можете проверить как работают эти вычисления с 
###  разными типами данных, например, сначала создать две переменные int, затем создать две 
###  переменные float и наконец создать переменные типа int и float и провести над ними 
###  операции, прописанные выше.

```python
a = 20
b = 12
print('Возведение в степень: ', a ** b)
print('Обычное деление: ', a / b)
print('Целочисленное деление: ', a // b)
print('Нахождение остатка от деления: ', a % b)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/6.png)

## Выводы
Я научился выполнять арифметические операции с помощью Python.

## Лабораторная работа №7
###  Создайте любую строковую переменную и произведите над ней математическое действие 
###  умножение на любое число.

```python
line = 'shot'
print(line * 5)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/7.png)

## Выводы
Я научился применять математические действия по отношению к строковым переменным.

## Лабораторная работа №8
### Посчитайте сколько раз символ ‘l’ встречается в строке ‘Hello World’.

```python
line = "Hello world"
print(line.count('l'))
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/8.png)

## Выводы
Я изучил и воспользовался методом count(). Этот метод может быть полезен для анализа текста или проверки наличия определенных символов в строке.

## Лабораторная работа №9
### Напишите предложение ‘Hello World’ в две строки. Написанная программа должна занимать 
### одну строку в редакторе кода.

```python
print('Hello\nWorld')
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/9.png)

## Выводы
Внутри скобок указан строковый литерал 'Hello\nWorld'.
\n - это специальный символ, обозначающий новую строку.

## Лабораторная работа №10
### Из предложения ‘Hello World’ выведите в консоль только 2 символ, а затем выведите слово 
### ‘Hello’

```python
line = 'Hello world'
print(line[1])
print(line[:5])
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/10.png)

## Выводы
Индексация в Python начинается с нуля, поэтому line[1] обращается к второму символу.
Срезы в Python используют синтаксис [start:end].
Оставление индекса до конца (:) означает выбор от начала строки до указанного индекса.

## Самостоятельная работа №1
###  Выведите в консоль булевую переменную False, не используя слово False в строке или 
###  изначально присвоенную булевую переменную. Программа должна занимать не более двух 
###  строк редактора кода.

```python
print(1>2)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/11.png)

## Выводы
При выполнении этого кода будет выведено значение False, так как число 1 меньше числа 2.

## Самостоятельная работа №2
###  Присвоить значения трем переменным и вывести их в консоль, используя только две строки 
###  редактора кода.

```python
name = 'Кирилл'; surname = 'Зеленцов' ; group = "ПИЭ-22-1"
print(name, surname, group)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/12.png)

## Выводы
Код определяет переменные name, surname и group, а затем выводит их значения с помощью функции print(). 

## Самостоятельная работа №3
### Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных 
### int). То есть при вводе буквенных символов в консоль, программа не должна работать. 
### Программа должна занимать не более двух строк редактора кода.

```python
number = int(input("Введите только целочисленные значения: "))
print(number)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/13.png)

## Выводы
Я изучил как приводить к типу данных в Python, а также как работает input(). 

## Самостоятельная работа №4
###  Создайте только одну строковую переменную. Длина строки должна не превышать 5 
###  символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа 
###  должна занимать не более двух строк редактора кода.

```python
a = "abcde"
print(a*5)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/14.png)

## Выводы
Функция print() в Python выводит результат выражения, которое находится перед ней. В этом случае, умножение строки a на число 5 создает новую строку, повторяющую исходную строку 5 раз.

## Самостоятельная работа №5
###  Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год 
###  (тип данных - числовой) и выведите в консоль текущую дату в формате: “Сегодня день месяц
###  год. Всего хорошего!” используя F строку и оператор end внутри print(), в котором вы должны 
###  написать фразу “Всего хорошего!”. Программа должна занимать не более двух строк 
###  редактора кода.

```python
day = 14; month = "Сентября"; year = 2024
print(f"Сегодня {day} {month} {year}.", end=" Всего хорошего!" )
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/15.png)

## Выводы
Этот код определяет дату и выводит ее в формате с русскими месячными названиями. Также используется форматированная строка (f-string) для создания выводимого сообщения. Здесь end используется для добавления дополнительного текста после вывода строки без переноса на новую строку.

## Самостоятельная работа №6
###  В предложении ‘Hello World’ вставьте ‘my’ между двумя словами. Выведите полученное 
###  предложение в консоль в одну строку. Программа должна занимать не более двух строк 
###  редактора кода.

```python
line = 'my'
print(f"Hello {line} world!")
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/16.png)

## Выводы
Строчку 'my' я занес в отдельную переменную, а потом с помощью форматированной строки (f-string) вставил в выводимую строчку.

## Самостоятельная работа №7
### Узнайте длину предложения ‘Hello World’, результат выведите в консоль. Программа должна 
### занимать не более двух строк редактора кода.

```python
line = 'Hello world'
print(len(line))
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/17.png)

## Выводы
Длину строки я узнаю с помощью функции len(). Она подсчитывает количество символов в строке.

## Самостоятельная работа №8
###  Переведите предложение ‘HELLO WORLD’ в нижний регистр. Программа должна занимать 
###  не более двух строк редактора кода.

```python
print("HELLO WORLD".lower())
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/18.png)

## Выводы
С помощью функции .lower() содержимое строки я перевел в нижний регистр.

## Самостоятельная работа №9
### Создайте три переменных с целочисленными значениями. Первые две переменные перемножьте и разделите полученный ответ на третью(деление должно быть целочисленным).

```python
a = 5
b = 10
c = 4
print((a*b)//c)
```

### Результат.
![Меню](hhttps://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/19.png)

## Выводы
Я научился выполнять арифметические операции с помощью Python. 

## Самостоятельная работа №10
### Создайте две строковые переменные. Выполните конкатенацию строк.

```python
line1 = 'Я люблю'
line2 = ' Python'
print(line1+line2)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/20.png)

## Выводы
Я научился складывать строки в Python. 

## Общие выводы по теме
Благодаря выполнению лабораторной и самостоятельной работ, я изучил базовый синтаксис языка Python, его базовые операции.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/111.png)
