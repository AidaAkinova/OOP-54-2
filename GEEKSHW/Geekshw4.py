from faker import Faker


def generate_fake_users(count=3):
    """
    Генерирует fake-пользователей с помощью библиотеки Faker

    Args:
        count (int): Количество пользователей для генерации

    Returns:
        list: Список словарей с данными пользователей
    """
    fake = Faker()
    users = []

    for _ in range(count):
        user = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'birthdate': fake.date_of_birth()
        }
        users.append(user)

    return users


if __name__ == "__main__":

    fake_users = generate_fake_users(3)


    for i, user in enumerate(fake_users, 1):
        print(f"\nПользователь #{i}:")
        for key, value in user.items():
            print(f"{key}: {value}")