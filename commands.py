from logger import log
from sender import send_message


def process_command(vk, message, user_id, group):

    text = message.get("text", "").strip()

    if not text.startswith("/"):
        return False

    if user_id not in group.get("admins", []):

        log(
            f"[{group['name']}] "
            f"Пользователь {user_id} попытался выполнить команду"
        )

        return True

    if text == "/status":

        send_message(
            vk,
            user_id,
            (
                "✅ VK AntiSpam Bot работает\n\n"
                f"Группа: {group['name']}\n"
                "Статус: Онлайн"
            )
        )

        log(
            f"[{group['name']}] "
            f"Администратор {user_id} запросил статус"
        )

        return True

    return False