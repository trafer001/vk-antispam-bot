from vk_api.bot_longpoll import VkBotEventType
from moderator import should_delete, get_user_role
from logger import log
from commands import process_command
from delete_message import delete_message
from stats import message_received, message_deleted


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

                message_received()

                message_id = message.get("id")
                peer_id = message.get("peer_id")
                user_id = message.get("from_id")
                text = message.get("text", "").strip()

                if user_id is None:

                    log(
                        f"[{group['name']}] "
                        "Не удалось определить пользователя"
                    )

                    continue

                role = get_user_role(user_id, group)

                if process_command(vk, message, user_id, group):
                    continue

                log(
                    f"[{group['name']}] "
                    f"ROLE={role} "
                    f"ID={message_id} "
                    f"PEER={peer_id} "
                    f"USER={user_id} "
                    f"TEXT={text}"
                )

                if should_delete(user_id, group):

                    if message_id is None:

                        log(
                            f"[{group['name']}] "
                            "Не удалось определить ID сообщения"
                        )

                        continue

                    success = delete_message(
                        vk,
                        group,
                        message_id
                    )

                    if success:

                        message_deleted()

                        log(
                            f"[{group['name']}] "
                            f"Сообщение пользователя {user_id} удалено"
                        )

                    else:

                        log(
                            f"[{group['name']}] "
                            f"Не удалось удалить сообщение {message_id}"
                        )

                else:

                    log(
                        f"[{group['name']}] "
                        f"Сообщение пользователя {user_id} разрешено"
                    )

        except Exception as error:

            log(
                f"[{group['name']}] "
                f"Ошибка Long Poll: {error}"