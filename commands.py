from logger import log
from sender import send_message
from moderator import is_admin


def process_command(vk, message, user_id, group):

    text = message.get("text", "").strip()

    if not text.startswith("/"):
        return False

    if not is_admin(user_id, group):

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

    if text == "/help":

        send_message(
            vk,
            user_id,
            (
                "📋 VK AntiSpam Bot\n\n"
                "Доступные команды:\n\n"
                "/status — статус бота\n"
                "/help — список команд\n"
                "/list — доверенные пользователи\n"
                "/trust ID — добавить пользователя\n"
                "/untrust ID — удалить пользователя"
            )
        )

        log(
            f"[{group['name']}] "
            f"Администратор {user_id} запросил помощь"
        )

        return True

    if text == "/list":

        trusted = group.get("trusted_users", [])

        if trusted:

            users = "\n".join(str(user) for user in trusted)

            answer = (
                "👥 Доверенные пользователи:\n\n"
                f"{users}"
            )

        else:

            answer = "Список доверенных пользователей пуст."

        send_message(
            vk,
            user_id,
            answer
        )

        log(
            f"[{group['name']}] "
            f"Администратор {user_id} запросил список доверенных пользователей"
        )

        return True

    send_message(
        vk,
        user_id,
        "Неизвестная команда.\nНапишите /help"
    )

    return True