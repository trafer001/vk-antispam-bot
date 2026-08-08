import time
from threading import Thread

from bot import start_bot
from config import load_groups
from vk_client import create_connection


def main():

    print("=" * 40)
    print("VK AntiSpam Bot")
    print("=" * 40)

    try:
        groups = load_groups()

    except Exception as error:

        print(f"Ошибка загрузки конфигурации: {error}")
        return

    print(f"Найдено групп: {len(groups)}")

    connections = []

    for group in groups:

        name = group.get(
            "name",
            "Без названия"
        )

        if not group.get("enabled", True):

            print(
                f"Группа отключена: {name}"
            )

            continue

        try:

            connection = create_connection(group)

            connections.append(connection)

        except Exception as error:

            print(
                f"Ошибка подключения "
                f"{name}: {error}"
            )

    print()

    print(
        f"Успешно подключено групп: "
        f"{len(connections)}"
    )

    if not connections:

        print(
            "Нет доступных групп для запуска."
        )

        return

    print("Инициализация завершена")
    print()
    print("Запуск модераторов...")

    threads = []

    for connection in connections:

        thread = Thread(
            target=start_bot,
            args=(connection,),
            daemon=True
        )

        thread.start()
        threads.append(thread)

    print("Все группы запущены.")

    try:

        while True:
            time.sleep(60)

    except KeyboardInterrupt:

        print()
        print("Остановка VK AntiSpam Bot...")


if __name__ == "__main__":
    main()
