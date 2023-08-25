"""Задание 1.
Создайте таблицу "Географическое распространение", которая будет содержать информацию о том,
где обитают определенные виды животных и растений. Поля могут включать: идентификационный номер животного или растения,
континент, страны, регионы и другие местоположения."""

# Создание таблицы через командную строку win10.
cd C:\Program Files\mysql\mysql server 8.0\bin

# Имя пользователя и пароль SQL сервера.
mysql -u root -p

# Создание базы данных.
CREATE DATABASE homework;

# Вход в базу данных.
USE homework;


# Создаёт таблицу с именами столбцов и типом данных которые можно туда вносить.
CREATE TABLE geographical_distribution(
              id INT AUTO_INCREMENT PRIMARY KEY, # Автоматическая нумерация столбцов при занесении данных.
              name VARCHAR(255),
              continent VARCHAR(255),
              countries VARCHAR(255),
              regions VARCHAR(255)
              );

# Занесение данный в таблицу.
INSERT INTO geographical_distribution(name, continent, countries, regions) values('Сурок', 'Евразия', 'США', 'Степи Азии и Европы');
INSERT INTO geographical_distribution(name, continent, countries, regions) values('Ромашка', 'Европа', 'Россия', 'Сибирь, Алтай, Забайкалье');
INSERT INTO geographical_distribution(name, continent, countries, regions) values('Тарантул', 'Южная Европа', 'Италия', 'Таранто');


"""Задание 2.
Создайте таблицу "Фотографии животных", которая будет содержать ссылки на фотографии разных видов животных. 
Поля могут включать: идентификационный номер животного и ссылку на фотографию."""

CREATE TABLE animal_pictures(
    -> id_animals INT AUTO_INCREMENT PRIMARY KEY,
    -> name VARCHAR(255),
    -> link_to_photo TEXT
    );

INSERT INTO animal_pictures(name, link_to_photo) values('Сурок', 'https://www.google.com/search?q=%D1%81%D1%83%D1%80%D0'
                                                                 '%BE%D0%BA&tbm=isch&ved=2ahUKEwix6f6J3fiAAxWupycCHVQND'
                                                                 'JsQ2-cCegQIABAA&oq=%D1%81%D1%83%D1%80%D0%BE%D0%BA&gs_'
                                                                 'lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFC'
                                                                 'AAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABD'
                                                                 'oHCAAQigUQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBUPoLWO4PYPk'
                                                                 'RaABwAHgAgAFQiAGMA5IBATaYAQCgAQGqAQtnd3Mtd2l6LWltZ8AB'
                                                                 'AQ&sclient=img&ei=fhnpZLGyE67PnsEP1Jqw2Ak&rlz=1C1GCEA'
                                                                 '_enBY932BY932');
INSERT INTO animal_pictures(name, link_to_photo) values('Тарантул', 'https://www.google.com/search?q=%D1%82%D0%B0%D1%80'
                                                                    '%D0%B0%D0%BD%D1%82%D1%83%D0%BB&tbm=isch&ved=2ahUKE'
                                                                    'wi7mLWF3PiAAxUqsCcCHbJoAosQ2-cCegQIABAA&oq=%D1%82%'
                                                                    'D0%B0%D1%80%D0%B0%D0%BD%D1%82%D1%83%D0%BB&gs_lcp=C'
                                                                    'gNpbWcQAzIECCMQJzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIAB'
                                                                    'ABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEO'
                                                                    'gcIABCKBRBDOgsIABCABBCxAxCDAToICAAQgAQQsQNQuRBYkRl'
                                                                    'guRtoAHAAeACAAYYBiAGjBZIBAzguMZgBAKABAaoBC2d3cy13a'
                                                                    'XotaW1nwAEB&sclient=img&ei=aBjpZLvEEargnsEPstGJ2Ag'
                                                                    '&rlz=1C1GCEA_enBY932BY932');