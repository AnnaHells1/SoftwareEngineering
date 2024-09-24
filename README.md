# Тема 3. Базовые операции языка Python
Отчет по Теме #3 выполнила:
- Кукурузняк А.Д.
- ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### 

```python
one = int(input("Введите значение первой переменной: "))
two = int(input("Введите значение второй переменной: "))
if one >= two:
    print("Выполняется")
else:
    print("Не выполняется")
```
### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/1.png)

## Выводы
С помощью print выводим строки в консоль. Чтобы вывести строчку - содержимое заносим в ковычки. 

## Лабораторная работа №2
### Выведите в консоль три строки. Первая – результат сложения или вычитания минимум двух переменных типа int. Вторая – результат сложения или вычитания минимум 
### двух переменных типа float. Третья – результат сложения или вычитания минимум двух переменных типа int и float.

```python
one = int(input("Введите значение первой переменной: "))
if one < 0:
    print("Переменная меньше 0")
elif 0 < one < 10:
    print("Перемнная больше 0 и меньше 10")
else:
    print("Переменная больше 10")
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
numbers = [1, 3, 4, 6, 8, 9]
value = int(input("Введите значение перемнной: "))
if value in numbers:
    print("Переменная есть в данном массиве")
else:
    print("Переменной нет в этом массиве")
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
numbers = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
value = int(input("Введите значение перемнной: "))
if value in numbers:
    if value % 2 == 0:
      print("Переменная четная и есть в данном массиве")
    else:
        print("Переменная нечетная и есть в данном массиве")
else:
    print(f"Переменной нет в этом массиве, и она равна {value}")
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/4.png)

## Выводы
Я изучил как приводить переменные к типам данных.

## Лабораторная работа №5
###  Присвойте трем переменным различные значения, воспользовавшись функцией input().

```python
for i in range(10):
    print("i = ", i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print("Переменная равна 2 или 3")
    elif i in [4, 5, 6]:
        print("Переменная равна 4, 5 или 6")
    else:
        break
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
string = "привет всем изучающим Phyton!"
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
else:
    print(f"Буквы '{value}' нет в указанной строке")
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/6.png)

## Выводы
Я научился выполнять арифметические операции с помощью Python.

## Лабораторная работа №7
###  Создайте любую строковую переменную и произведите над ней математическое действие 
###  умножение на любое число.

```python
value = 100
for i in range(10, -1, -1):
    value -= i
    print(i, value)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/7.png)

## Выводы
Я научился применять математические действия по отношению к строковым переменным.

## Лабораторная работа №8
### Посчитайте сколько раз символ ‘l’ встречается в строке ‘Hello World’.

```python
value = 0
while value < 100:
    if value == 0:
        value += 10
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5
    print(value)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/8.png)

## Выводы
Я изучил и воспользовался методом count(). Этот метод может быть полезен для анализа текста или проверки наличия определенных символов в строке.

## Лабораторная работа №9
### Напишите предложение ‘Hello World’ в две строки. Написанная программа должна занимать 
### одну строку в редакторе кода.

```python
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)
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
even_array = [2, 4, 6, 8, 9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print("В массиве есть нечетное число")
else:
    print("В массиве все числа четные")
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
a = 1
for i in range(2):
    a*=5
    a+=1
print(a)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/11.png)

## Выводы
При выполнении этого кода будет выведено значение False, так как число 1 меньше числа 2.

## Самостоятельная работа №2
###  Присвоить значения трем переменным и вывести их в консоль, используя только две строки 
###  редактора кода.

```python
for letter in reversed("Hello World"):
    print(letter)
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
c = int(input("Введите число от 0 до 10: "))
if c>10 or c<0:
    print("Числе не в диапазоне.")
elif (c >= 0 and c < 4):
    print("От 0 до 3")
elif (c >= 4 and c < 6):
    print("От 3 до 6")
elif (c >= 6 and c < 11):
    print("От 6 до 10")
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
Phrase = input("Напишите предложение на английском: ").lower()
Quantity = 0
for letter in Phrase:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        Quantity+=1
NewPhrase = Phrase.replace("ugly", "beauty")
print(f"Длина предложения = {len(Phrase)} символов. \nКоличество искомых гласных = {Quantity}. \nНовая фраза = {NewPhrase}."
      f"\n Начинается ли предложение с The - {NewPhrase.startswith('The')}. \nЗаканчивается ли на end - {NewPhrase.endswith('end')}")
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
counter = 0
string = 'hello'
values = [0,2,4,6,8,10]
while counter != 10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    string = memory
    counter+=1
memory = ' world'
print(string + memory)
```

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/15.png)

## Выводы
Этот код определяет дату и выводит ее в формате с русскими месячными названиями. Также используется форматированная строка (f-string) для создания выводимого сообщения. Здесь end используется для добавления дополнительного текста после вывода строки без переноса на новую строку.

## Выводы
Я научился складывать строки в Python. 

## Общие выводы по теме
Благодаря выполнению лабораторной и самостоятельной работ, я изучил базовый синтаксис языка Python, его базовые операции.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_2/Pic/111.png)
