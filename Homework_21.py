"""Задание
У вас есть онлайн-магазин, который продает электронику. Компания имеет следующие сущности:

Пользователи (Users):
user_id (уникальный идентификатор пользователя)
имя (first_name)
фамилия (last_name)
электронная почта (email)
адрес доставки (shipping_address)

Продукты (Products):
product_id (уникальный идентификатор продукта)
название (name)
категория (category)
бренд (brand)
цена (price)
количество на складе (quantity)

Заказы (Orders):
order_id (уникальный идентификатор заказа)
user_id (идентификатор пользователя, связь с таблицей Users)
дата (date)
статус (status)

Позиции заказов (OrderItems):
order_items_id (уникальный идентификатор позиции заказа)
order_id (идентификатор заказа, связь с таблицей Orders)
product_id (идентификатор продукта, связь с таблицей Products)
количество (quantity)
стоимость (price)

В каждую таблицу добавьте по 10 записей и решите следующие задачи:
1. Найти все заказы, сделанные определённым пользователем (по его электронной почте).
2. Подсчитать общее количество продуктов в определённой категории.
3. Найти все заказы, сделанные в определённый период времени.
4. Подсчитать сумму всех заказов для каждого пользователя.
5. Найти все продукты, у которых остаток на складе меньше определённого значения.
6. Найти все заказы, стоимость которых превышает определённую сумму.
7. Найти все заказы, которые находятся в определённом статусе.
8. Подсчитать среднюю стоимость продуктов в каждой категории.
9. Найти все заказы, которые содержат определённый продукт.
10. Подсчитать общую стоимость всех заказов, сделанных в определённом году."""

cd C:\Program Files\mysql\mysql server 8.0\bin
mysql -u root -p

USE homework;

CREATE TABLE users(
    -> user_id INT PRIMARY KEY,
    -> first_name VARCHAR(20),
    -> last_name VARCHAR(20),
    -> email VARCHAR(50),
    -> shipping_adress VARCHAR(100));

CREATE TABLE products(
    -> product_id INT PRIMARY KEY,
    -> name VARCHAR(20),
    -> category VARCHAR(20),
    -> brand VARCHAR(20),
    -> price FLOAT,
    -> quantity INT);

CREATE TABLE orders(
    -> order_id INT PRIMARY KEY,
    -> user_id INT,
    -> date DATE,
    -> status VARCHAR(20),
    -> FOREIGN KEY(order_id) REFERENCES users(user_id)
    -> );

CREATE TABLE orderitems(
    -> order_items_id INT PRIMARY KEY,
    -> order_id INT,
    -> product_id INT,
    -> quantity INT,
    -> price FLOAT,
    -> FOREIGN KEY(order_id) REFERENCES orders(order_id),
    -> FOREIGN KEY(product_id) REFERENCES products(product_id)
    -> );

INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(1,'Валера','Пупкин','pupkin@gmail.com', 'улица Свободы дом 18 квартира 3');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(2,'Вася','Ножкин','nojkin@gmail.com', 'улица Московская дом 36 квартира 84');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(3,'Петя','Калкин','kalkin@gmail.com', 'улица Просторная дом 3 квартира 128');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(4,'Анатолий','Кускевич','kuskevich@gmail.com', 'улица Радиаторная дом 23 квартира 30');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(5,'Роман','Картошкин','kartoshkin@gmail.com', 'улица Запретная дом 29 квартира 68');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(6,'Федя','Апельсинов','apelsinov@gmail.com', 'улица Фруктовая дом 9 квартира 18');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(7,'Толя','Мандаринкин','mandarinkin@gmail.com', 'улица Фруктовая дом 9 квартира 19');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(8,'Коля','Сыроежкин','siroezhkin@gmail.com', 'улица Грибная дом 2 квартира 54');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(9,'Святослав','Тараев','taraev@gmail.com', 'улица Мирная дом 10 квартира 11');
INSERT INTO users(user_id, first_name, last_name, email, shipping_adress) values(10,'Илья','Курочкин','kurochkin@gmail.com', 'улица Сельхозная дом 1 квартира 2');

INSERT INTO products(product_id, name, category, brand, price, quantity) values(1,'Компьтерная мышка','Компьютеры',' GYGABYTE', 70, 20);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(2,'Компьютерная клавиатура','Компьютеры','GYGABYTE', 120, 20);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(3,'Компьютерные колонки','Компьютеры','SVEN огруец', 170, 10);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(4,'Наушники проводные','Гарнитура','Xiaomi', 40, 20);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(5,'Наушники беспроводные','Гарнитура','Xiaomi', 90, 50);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(6,'Компьютер','Компьютеры','ASUS', 5300, 3);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(7,'Ноутбук','Компьютеры','Lenovo', 3000, 5);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(8,'Телевизор','Телевизоры','LG', 1700, 7);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(9,'Мобильный телефон','Телефоны','Apple', 2200, 10);
INSERT INTO products(product_id, name, category, brand, price, quantity) values(10,'Планшет','Планшеты','Lenovo', 800, 10);

INSERT INTO orders(order_id, user_id, date, status) values(1, 1, '2022-12-25', 'Выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(2, 2, '2023-02-27', 'Выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(3, 3, '2023-08-14', 'Выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(4, 3, '2023-08-20', 'Выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(5, 7, '2023-08-25', 'Выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(6, 9, '2023-08-30', 'Не выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(7, 5, '2023-09-10', 'Не выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(8, 3, '2023-09-10', 'Не выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(9, 1, '2023-09-11', 'Не выполнен');
INSERT INTO orders(order_id, user_id, date, status) values(10, 8, '2023-09-15', 'Не выполнен');

INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(1, 1, 1, 2, 2*70);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(2, 1, 8, 1, 1*120);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(3, 2, 9, 2, 2*170);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(4, 2, 10, 2, 2*40);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(5, 3, 3, 1, 1*90);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(6, 3, 4, 1, 1*5300);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(7, 3, 5, 1, 1*3000);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(8, 4, 6, 1, 1*1700);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(9, 5, 9, 2, 2*2200);
INSERT INTO orderitems(order_items_id, order_id, product_id, quantity, price) values(10, 6, 2, 3, 3*800);

# 1. Найти все заказы, сделанные определённым пользователем (по его электронной почте).
SELECT * FROM users;
SELECT * FROM orders WHERE user_id = 3;

# 2. Подсчитать общее количество продуктов в определённой категории.
SELECT SUM(quantity) FROM products WHERE category LIKE 'К%';

# 3. Найти все заказы, сделанные в определённый период времени.
SELECT * FROM orders WHERE date > '2023-01-01' AND date < '2023-08-25';

# 4. Подсчитать сумму всех заказов для каждого пользователя.
SELECT * FROM orders WHERE user_id = 1;
SELECT SUM(price) FROM orderitems WHERE (order_id = 1) + (order_id = 9);

SELECT * FROM orders WHERE user_id = 2;
SELECT SUM(price) FROM orderitems WHERE order_id = 2;

SELECT * FROM orders WHERE user_id = 3;
SELECT SUM(price) FROM orderitems WHERE (order_id = 3) + (order_id = 4) + (order_id = 8);

SELECT * FROM orders WHERE user_id = 4;
Empty set (0.00 sec)

SELECT * FROM orders WHERE user_id = 5;
SELECT SUM(price) FROM orderitems WHERE order_id = 7;

SELECT * FROM orders WHERE user_id = 6;
Empty set (0.00 sec)

SELECT * FROM orders WHERE user_id = 7;
SELECT SUM(price) FROM orderitems WHERE order_id = 5;

SELECT * FROM orders WHERE user_id = 8;
SELECT SUM(price) FROM orderitems WHERE order_id = 10;

SELECT * FROM orders WHERE user_id = 9;
SELECT SUM(price) FROM orderitems WHERE order_id = 6;

SELECT * FROM orders WHERE user_id = 10;
Empty set (0.00 sec)

# 5. Найти все продукты, у которых остаток на складе меньше определённого значения.
SELECT product_id FROM orderitems;

# 6. Найти все заказы, стоимость которых превышает определённую сумму.
SELECT order_id FROM orderitems WHERE price < 2000;

# 7. Найти все заказы, которые находятся в определённом статусе.
SELECT * FROM orders WHERE status = 'Не выполнен';

# 8. Подсчитать среднюю стоимость продуктов в каждой категории.
SELECT SUM(price/2) FROM products WHERE category = 'Компьютеры';
SELECT SUM(price/2) FROM products WHERE category = 'Гарнитура';
SELECT SUM(price/2) FROM products WHERE category = 'Телевизоры';
SELECT SUM(price/2) FROM products WHERE category = 'Телефоны';
SELECT SUM(price/2) FROM products WHERE category = 'Планшеты';

# 9. Найти все заказы, которые содержат определённый продукт.
SELECT product_id FROM products WHERE name = 'Компьютер';
SELECT order_id FROM orderitems WHERE product_id = 6;
SELECT * FROM orders WHERE order_id = 6;

# 10. Подсчитать общую стоимость всех заказов, сделанных в определённом году.
SELECT order_id FROM orders WHERE date LIKE '2023%';
SELECT SUM(price) FROM orderitems WHERE (order_id = 2) + (order_id = 3) + (order_id = 4) + (order_id = 5) + (order_id = 6) + (order_id = 7) + (order_id = 8) + (order_id = 9) + (order_id = 10);