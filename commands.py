from logger import log


def process_command(message, user_id, group):

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

        log(
            f"[{group['name']}] "
            f"Запрошен статус бота"
        )

        return True

    return False