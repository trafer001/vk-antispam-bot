from vk_api.bot_longpoll import VkBotEventType
from moderator import should_delete
from logger import log


def start_bot(connection):

    vk = connection["vk"]
    longpoll = connection["longpoll"]
    group = connection["group"]

    log(f"Запущен модератор: {group['name']}")

    while True:

        try:

            for event in longpoll.listen():

                if event.type != VkBotEventType.MESSAGE_NEW:
                    continue

                message = event.object.message

                message_id = message["id"]
                peer_id = message["peer_id"]

                user_id = message["from_id"]
                text = message.get("text", "")

                log(
                    f"[{group['name']}] "
                    f"ID={message_id} "
                    f"PEER={peer_id} "
                    f"USER={user_id} "
                    f"TEXT={text}"
                )

                if should_delete(user_id, group):

                    log(
                        f"[{group['name']}] "
                        f"Сообщение пользователя {user_id} "
                        f"помечено к удалению"
                    )

        except Exception as error:

            log(
                f"[{group['name']}] Ошибка Long Poll: {error}"
            )