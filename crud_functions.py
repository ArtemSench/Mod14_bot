import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def upload_db():
    products = [
        ('Банка', 'какая-то банка', 1000000),
        ('Бутылка', 'для лечения депрессии', 1000000000),
        ('ЗупЫрЁк', 'непонятная шняга', 1),
        ('Таблетки', 'пофиг', 100)
    ]
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products



