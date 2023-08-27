"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import pathlib
from csv import DictReader

# Путь к рабочей директории для поиска файлов
path = pathlib.Path(os.getcwd(), 'north_data')


def search_files(path_to_file):
    """
    Функция ищет в рабочей папке файлы с расширением .csv
    path_to_file: путь к рабочей директории.
    return: список с именами файлов.
    """
    # Переменная для хранения имён файлов
    list_with_files = []
    # В цикле пробегаем по рабочей директории с помощью функции walk() библиотеки os
    # и выбираем файлы с нужным расширением.
    for rootdir, dirts, files in os.walk(path_to_file):
        for file in files:
            if file.split('.')[-1] == 'csv':
                list_with_files.append(file)
    return list_with_files


def get_data_from_csv_files(list_files):
    """
    Функция ищет нужный файл и заносит данные из файла в соответствующую таблицу в БД.
    list_file: Список с именами файлов.
    """
    # Пробегаем по списку с именами и находим нужные файлы по ключевым словам.
    for file in list_files:
        if 'customers' in file:
            # В случае нахождения получаем данные из файла в экземпляр класса DictReader и передаём в функцию для
            # записи в БД.
            with open(f'{path}\\{file}') as csvfile:
                reader = DictReader(csvfile)
                writing_data_in_customers_table(reader)
        elif 'employees' in file:
            with open(f'{path}\\{file}') as csvfile:
                reader = DictReader(csvfile)
                writing_data_in_employees_table(reader)
        elif 'orders' in file:
            with open(f'{path}\\{file}') as csvfile:
                reader = DictReader(csvfile)
                writing_data_in_orders_table(reader)


def writing_data_in_customers_table(dict_with_data):
    """
    Функция для записи данных из файла customers_data
    """
    # Устанавливаем соединение с БД
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )
    cur = conn.cursor()

    # Пробегаемся по списку с данными для записи каждой строки
    for row in dict_with_data:
        # Переменная для шаблона запроса к БД
        database_query = """INSERT INTO customers_data VALUES(%s, %s, %s)"""
        # Переменная для хранения и передачи данных для записи в БД
        values_to_insert = tuple(row.values())
        cur.execute(database_query, values_to_insert)
        conn.commit()

    cur.close()
    conn.close()


def writing_data_in_employees_table(dict_with_data):
    """
    Функция для записи данных из файла employees_data.csv
    """
    # Соединения с БД
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )
    cur = conn.cursor()

    # Пробегаемся по списку строк
    for row in dict_with_data:
        # Шаблон запроса к БД
        database_query = """INSERT INTO employee_data VALUES(%s, %s, %s, %s, %s, %s)"""
        # Переменная для записи данных в БД
        values_to_insert = tuple(row.values())
        cur.execute(database_query, values_to_insert)
        conn.commit()
    cur.close()
    conn.close()


def writing_data_in_orders_table(dict_with_data):
    """
    Функция для записи данных из файла orders_data.csv
    """
    # Соединения с БД
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )

    cur = conn.cursor()
    # Пробегаемся по списку строк
    for row in dict_with_data:
        # Шаблон запроса к БД
        database_query = """INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)"""
        # Переменная для записи данных в БД
        values_to_insert = tuple(row.values())
        cur.execute(database_query, values_to_insert)
        conn.commit()
    cur.close()
    conn.close()


# Вызываем функцию для нахождения файлов в рабочей директории
list_files = search_files(path)
# Вызываем функцию для получения данных из найденных файлов
get_data_from_csv_files(list_files)
