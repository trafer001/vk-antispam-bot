from vk_api.bot_longpoll import VkBotEventType
from moderator import should_delete


def start_bot(connection):

    vk = connection["vk"]
    longpoll = connection["longpoll"]
    group = connection["group"]

    print(f"Запущен модератор: {group['name']}")

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            message = event.object.message

            user_id = message["from_id"]
            peer_id = message["peer_id"]

            text = message.get("text", "")

            print(
                f"[{group['name']}] "
                f"{user_id}: {text}"
            )

            if should_delete(user_id, group):

                try:

                    vk.messages.delete(
                        message_ids=message["id"]
                    )

                    print(
                        "Удалено сообщение:",
                        message["id"]
                    )

                except Exception as error:

                    print(
                        "Ошибка удаления:",
                        error
                    )