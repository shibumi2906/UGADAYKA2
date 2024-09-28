from core.utils.db import init_db

# Инициализация базы данных и создание таблиц
if __name__ == "__main__":
    init_db()
    print("База данных успешно создана!")
