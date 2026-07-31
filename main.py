from config import load_groups
from vk_client import create_connection

print("=" * 40)
print("VK AntiSpam Bot")
print("=" * 40)

groups = load_groups()

print(f"Найдено групп: {len(groups)}")

connections = []

for group in groups:

    if not group.get("enabled", True):
        continue

    try:

        connection = create_connection(group)

        connections.append(connection)

    except Exception as e:

        print(f"Ошибка подключения {group['name']}: {e}")

print()

print(f"Успешно подключено групп: {len(connections)}")
print("Инициализация завершена")