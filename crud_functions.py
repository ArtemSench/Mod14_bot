import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    conn = sqlite3.connect('users.db')
    curs = conn.cursor()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    curs.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    conn.commit()
    connection.close()
    conn.close()

def add_user(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True

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



