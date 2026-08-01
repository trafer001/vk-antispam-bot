from vk_api.bot_longpoll import VkBotEventType
from moderator import should_delete


def start_bot(connection):

    vk = connection["vk"]
    longpoll = connection["longpoll"]
    group = connection["group"]

    print(f"Запущен модератор: {group['name']}")

    while True:
        
        
        

    try:
        
        
        

        for event in longpoll.listen():

            if event.type != VkBotEventType.MESSAGE_NEW:
                continue

            message = event.object.message

            user_id = message["from_id"]
            text = message.get("text", "")

            print(
                f"[{group['name']}] "
                f"{user_id}: {text}"
            )

            if should_delete(user_id, group):

                print("Сообщение помечено к удалению")

    except Exception as error:

        print(
            f"[{group['name']}] Ошибка Long Poll:",
            error
        )