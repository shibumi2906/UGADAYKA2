# Функция для валидации данных
def validate_data(data):
    if not data:
        raise ValueError("Данные не могут быть пустыми")
    return True

# Функция для форматирования строк
def format_string(input_str):
    return input_str.strip().capitalize()

# Функция для проверки корректности числовых данных
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
