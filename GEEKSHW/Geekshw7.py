import sqlite3


def get_user_by_id(user_id):
    """
    Функция для поиска пользователя по ID в базе данных SQLite

    Args:
        user_id (int): ID пользователя для поиска

    Returns:
        dict or None: Возвращает данные пользователя в виде словаря, если найден,
                     или None, если пользователь не найден
    """
    conn = None
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, user_data))
        else:
            print(f"Пользователь с ID {user_id} не найден")
            return None

    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
        return None

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'Иван Иванов', 'ivan@example.com')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'Петр Петров', 'petr@example.com')")
    conn.commit()
    conn.close()


    print(get_user_by_id(1))
    print(get_user_by_id(3))