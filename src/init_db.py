import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(__file__), 'db', 'database.db')

    # Убедитесь, что папка db существует
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Создание таблицы
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        # Вставка данных
        cursor.execute('''
            INSERT INTO users (name, email) VALUES (?, ?)
        ''', ('Иван Иванов', 'ivan@example.com'))

        # Получение данных
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
        for row in results:
            print(row)

if __name__ == '__main__':
    main()

