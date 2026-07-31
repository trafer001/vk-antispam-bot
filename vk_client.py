import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


def create_connection(group):
    """Создает подключение к одной группе"""

    token = group["token"]
    group_id = group["group_id"]

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