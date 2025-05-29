import sqlite3

db = sqlite3.connect('school.db')
cursor = db.cursor()

def create_good_students_view():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS good_students AS
    SELECT users.id, users.name, AVG(grades.grade) as avg_grade
    FROM users
    JOIN grades ON users.id = grades.user_id
    GROUP BY users.id
    HAVING avg_grade > 4.5
    ''')
    print("Создано представление для хороших студентов!")


def show_good_students():
    cursor.execute('SELECT * FROM good_students')
    print("\nЛучшие студенты:")
    for student in cursor.fetchall():
        print(f"ID: {student[0]}, Имя: {student[1]}, Средний балл: {student[2]:.1f}")

def create_active_students_view():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS active_students AS
    SELECT users.id, users.name, COUNT(DISTINCT grades.subject) as subjects
    FROM users
    JOIN grades ON users.id = grades.user_id
    GROUP BY users.id
    ORDER BY subjects DESC
    LIMIT 5
    ''')
    print("\nСоздано представление для активных студентов!")

def show_active_students():
    cursor.execute('SELECT * FROM active_students')
    print("\nСамые активные студенты:")
    for student in cursor.fetchall():
        print(f"ID: {student[0]}, Имя: {student[1]}, Предметов: {student[2]}")


print("Начинаем работу с базой данных студентов")
create_good_students_view()
create_active_students_view()

show_good_students()
show_active_students()


db.close()
print("\nРабота с базой завершена!")