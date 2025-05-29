
import sqlite3


def get_user_by_id(user_id):
    """
    Функция для поиска пользователя по ID в базе данных.

    Args:
        user_id (int): ID пользователя для поиска

    Returns:
        dict or None: Возвращает данные пользователя в виде словаря, если найден,
                     или None, если пользователь не найден
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
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
        conn.close()


if __name__ == "__main__":
    user = get_user_by_id(1)
    print(user)