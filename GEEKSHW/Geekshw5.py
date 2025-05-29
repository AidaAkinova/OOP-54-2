def require_admin(func):
    def wrapper(user):
        if user.get('is_admin', False):
            return func(user)
        else:
            print("Access denied")

    return wrapper


@require_admin
def delete_user(user):
    print(f"User {user['name']} deleted")



def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result

    return wrapper


@logger
def say_hello():
    print("Hello!")



if __name__ == "__main__":
    print("=== Тест декоратора require_admin ===")
    delete_user({"name": "John", "is_admin": True})
    delete_user({"name": "Alice", "is_admin": False})

    print("\n=== Тест декоратора logger ===")
    say_hello()