import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


def create_connection(group):
    """Создает подключение к одной группе"""

    token = group.get("token")
group_id = group.get("group_id")

if not token:
    raise ValueError("Не указан token")

if not group_id:
    raise ValueError("Не указан group_id")

    vk_session = vk_api.VkApi(token=token)

    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(
        vk_session,
        group_id
    )

    print(f"✅ Подключена группа: {group['name']}")

    return {
        "vk": vk,
        "longpoll": longpoll,
        "group": group
    }