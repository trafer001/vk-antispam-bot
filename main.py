import time

from threading import Thread
from bot import start_bot
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

if not connections:
    print("Нет доступных групп для запуска.")
    exit()

print("Инициализация завершена")
print()

print("Запуск модераторов...")

for connection in connections:

    thread = Thread(
        target=start_bot,
        args=(connection,),
        daemon=True
    )

    thread.start()

print("Все группы запущены.")

while True:
    time.sleep(1)