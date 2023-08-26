"""Задача 1.
Создайте таблицу "Книги" со следующими полями:
id (целое число, первичный ключ)
название (строка)
автор (строка)
жанр (строка)
год издания (целое число)"""

cd C:\Program Files\mysql\mysql server 8.0\bin
mysql -u root -p

# Входит в созданную базу данных.
USE homework;

# Создаёт таблицу.
CREATE TABLE books(
    -> id INT PRIMARY KEY,
    -> name VARCHAR(20),
    -> autor VARCHAR(50),
    -> genre VARCHAR(20),
    -> the_year_of_publishing INT);

# Занесение данный в таблицу.
INSERT INTO books(id, name, autor, genre, the_year_of_publishing) values(1, 'Робинзон Крузо', 'Дениель Дэфо', 'Роман', 1719);
INSERT INTO books(id, name, autor, genre, the_year_of_publishing) values(2, 'Том Сойер', 'Марк Твен', 'Повесть', 1896);
INSERT INTO books(id, name, autor, genre, the_year_of_publishing) values(3, 'Мастер и Маргарита', 'Михаил Булгаков', 'Роман', 1966);

# Просмотр таблицы.
mysql> SELECT * FROM books;
+----+--------------------+-----------------+---------+------------------------+
| id | name               | autor           | genre   | the_year_of_publishing |
+----+--------------------+-----------------+---------+------------------------+
|  1 | Робинзон Крузо     | Дениель Дэфо    | Роман   |                   1719 |
|  2 | Том Сойер          | Марк Твен       | Повесть |                   1896 |
|  3 | Мастер и Маргарита | Михаил Булгаков | Роман   |                   1966 |
+----+--------------------+-----------------+---------+------------------------+

"""Задача 2.
Создайте таблицу "Задачи" со следующими полями:
id (целое число, первичный ключ)
название (строка)
описание (строка)
дата начала (дата)
дата окончания (дата)
статус (строка)"""

CREATE TABLE tasks(
    -> id INT PRIMARY KEY,
    -> name VARCHAR(20),
    -> description VARCHAR(255),
    -> start_date DATE,
    -> end_date DATE,
    -> status VARCHAR(20));

INSERT INTO tasks(id, name, description, start_date, end_date, status) values(1, 'Создать базу данных',
    'Создайте базу данных используя командную строку вашей операционной системы, предварительно установив MySQL сервер',
    '2023-08-20', '2023-08-21', 'Выполнено');
INSERT INTO tasks(id, name, description, start_date, end_date, status) values(2, 'Создать таблицу',
    'Создайте таблицу в созданной базе данных', '2023-08-21', '2023-08-22', 'Выполнено');
INSERT INTO tasks(id, name, description, start_date, end_date, status) values(3, 'Вывести таблицу',
    'Выведите созданную таблицу на экран', '2023-08-22', '2023-08-23', 'Не выполнено');

# Выводит таблицу на экран.
SELECT * FROM tasks;

"""Задача 3.
Создайте таблицу "Фильмы" со следующими полями: 
id (целое число, первичный ключ) 
название (строка)
режиссер (строка)
год выпуска (целое число) 
рейтинг (десятичное число)
длительность (целое число)"""

CREATE TABLE films(
    -> id INT PRIMARY KEY,
    -> name VARCHAR(50),
    -> director VARCHAR(50),
    -> year_of_issue INT,
    -> rating FLOAT,
    -> duration INT);

INSERT INTO films(id, name, director,year_of_issue, rating, duration) values(1, 'Аватар 2', 'Джеймс Кэмерон', 2022, 7.8, 192);
INSERT INTO films(id, name, director,year_of_issue, rating, duration) values(2, 'Зелёная миля', 'Фрэнк Дарабонт', 1999, 9,1, 189);
INSERT INTO films(id, name, director,year_of_issue, rating, duration) values(3, '1+1', 'Оливье Накаш', 2011, 8,8, 112);

SELECT * FROM films;
