import sqlite3


def initiate_db():
    connection = sqlite3.connect('database_tg.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    connection = sqlite3.connect('database_tg.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')

    products = cursor.fetchall()

    connection.close()
    return products
