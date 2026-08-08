import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


def create_connection(group):
    """Создаёт подключение к одной группе VK."""

    name = group.get("name", "Без названия")
    token = group.get("token")
    group_id = group.get("group_id")

    if not token:
        raise ValueError(
            f"[{name}] Не указан token"
        )

    if not group_id:
        raise ValueError(
            f"[{name}] Не указан group_id"
        )

    try:
        group_id = int(group_id)
    except (TypeError, ValueError) as error:
        raise ValueError(
            f"[{name}] group_id должен быть числом"
        ) from error

    try:

        vk_session = vk_api.VkApi(
            token=token
        )

        vk = vk_session.get_api()

        # Проверяем токен и доступ к группе.
        vk.groups.getById(
            group_id=group_id
        )

        longpoll = VkBotLongPoll(
            vk_session,
            group_id
        )

    except Exception as error:

        raise RuntimeError(
            f"[{name}] Не удалось подключиться к VK: {error}"
        ) from error

    print(
        f"✅ Подключена группа: {name}"
    )

    return {
        "vk": vk,
        "longpoll": longpoll,
        "group": group
    }
