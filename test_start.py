from config import load_groups
from vk_client import create_connection

print("=" * 40)
print("Проверка VK AntiSpam Bot")
print("=" * 40)

groups = load_groups()

print(f"Найдено групп: {len(groups)}")

for group in groups:

    try:

        create_connection(group)

        print(f"✓ {group['name']} подключена")

    except Exception as error:

        print(f"✗ Ошибка: {error}")

print()
print("Проверка завершена.")