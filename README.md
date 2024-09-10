# Тема 1. Введение в Python
Отчет по Теме #1 выполнил:
- Кукурузняк Анна Дмитриевна
- ПИЭ-22-1

| Задание | Лаб_раб | 
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Задание 1
### Установка

### Результат.
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/1.png)
## Выводы
Git установлен.

## Задание 2
### Настройка
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/2.png)
## Выводы
Можно настроить личные данные, редактор, а также просматривать список настроек с помощью команды git config --list.

## Задание 3
### Создание нового репозитория
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/3.png)
## Выводы
Для связи между локальным репозиторием и удалённым нужно инициализирвоать репозиторий локально.
  
## Задание 4
### Подготовка файлов
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/4.png)
## Выводы
Есть команды для добавления одного файла и проверки статуса файлов.

## Задание 5
### Фиксация изменений
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/5.png)
## Выводы
Для фиксации изменений используем команду git commit.
Для просмотра коммитов используем команду git log.

## Задание 6
### Подключение к удаленному репозиторию
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/6.png)
## Выводы
Подключение к удалённому репозиторию происходит с помощью команды git remote add origin URL.
С помощью git push добавляем изменения в удалённый репозиторий.
С помощью git pull извлекаем изменения.
Незафиксированные изменения можно сохранять с помощью git stash.

## Задание 7
### Ветвление
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/7.png)
## Выводы
Ветвление используется для организации работы по разным направлениям (веткам).
git branch название_ветки - cоздание ветки.
git checkout / git switch - переключение между ветками.
git merge - слияние веток.


## Задание 8
### Особенности применения «Фетч»
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/8.png)
## Выводы
git fetch извлекает изменения из удалённого репозитория, но не объединяет их с локальной веткой.
git fetch [Удалённый репозиторий].

## Задание 9
### Удаление файлов, веток, локальных и удалённых репозиториев
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/9.png)
## Выводы
git rm [название файла] - удалить файл.
git rm --cached [название файла] - удалить файл из индекса.
git branch -D - принудительное удаление локальной ветки.
git push origin --delete [название ветки] - удаление ветки.

## Задание 10
### Отслеживание изменений в коммитах
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/10.png)
## Выводы
git log / git diff - команды для отслеживания изменений в коммитах.

## Задание 11
### Возвращение файла к предыдущему (определенному) состоянию
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/11.png)
## Выводы
git checkout [хэш коммита] -- [путь к файлу] - возвращение файла к предыдущему состоянию (на момент указанного комимта).
-m - флаг, позволяющий оставить описание коммиту во время его создания.
  
## Задание 12
### Возвращение к предыдущему коммиту
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/12.png)
## Выводы
git reset --soft - сброс до предыдущего коммита (с сохранением изменений в рабочей директории).
git reset --hard - сброс до предыдущего коммита (с потерей изменений).
git reset --hard [хэш коммита] - сброс до конкретного коммита.
  
## Задание 13
### Исправление коммита
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/13.png)
## Выводы
После выполнение команды git commit --amend откроется текстовый редактор для редакции сообщения или добавления файлов. После внесения изменений коммит будет исправлен.
  
## Задание 14
### Разрешение конфликтов при слиянии
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/14.png)
В данном случае нет конфликтов, потмоу что происходит слияние между одной и той же веткой.
## Выводы
Разрешение конфликтов при слиянии включает в себя изменение кода, чтобы устранить конфликты, и продолжить слияние после их разрешения.
  
## Задание 15
### Настройка .gitignore
![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/15.png)
## Выводы
Файл .gitignore - важная составляющая каждого репозитория
Преимущества использования:
#### Исключение ненужных файлов;
#### Сокращение размера репозитория;
#### Соблюдение принципов безопасности;
#### Сохранение чистоты репозитория.

![Меню](https://github.com/AnnaHells1/SoftwareEngineering/blob/main/Pic/111.png)
