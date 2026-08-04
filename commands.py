from logger import log
from sender import send_message
from moderator import is_admin
from config import load_groups, save_groups


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

        return True

    if text == "/help":

        send_message(
            vk,
            user_id,
            (
                "📋 VK AntiSpam Bot\n\n"
                "Команды:\n"
                "/status\n"
                "/help\n"
                "/list\n"
                "/trust ID\n"
                "/untrust ID"
            )
        )

        return True

    if text == "/list":

        trusted = group.get("trusted_users", [])

        if trusted:

            answer = "👥 Доверенные:\n\n"

            answer += "\n".join(
                str(user)
                for user in trusted
            )

        else:

            answer = "Список пуст."

        send_message(
            vk,
            user_id,
            answer
        )

        return True

    if text.startswith("/trust "):

        try:

            trusted_id = int(
                text.split()[1]
            )

        except:

            send_message(
                vk,
                user_id,
                "Неверный ID."
            )

            return True

        if trusted_id not in group["trusted_users"]:

            group["trusted_users"].append(
                trusted_id
            )

            groups = load_groups()

            for item in groups:

                if item["group_id"] == group["group_id"]:

                    item["trusted_users"] = group["trusted_users"]

            save_groups(groups)

        send_message(
            vk,
            user_id,
            "Пользователь добавлен."
        )

        return True

    if text.startswith("/untrust "):

        try:

            trusted_id = int(
                text.split()[1]
            )

        except:

            send_message(
                vk,
                user_id,
                "Неверный ID."
            )

            return True

        if trusted_id in group["trusted_users"]:

            group["trusted_users"].remove(
                trusted_id
            )

            groups = load_groups()

            for item in groups:

                if item["group_id"] == group["group_id"]:

                    item["trusted_users"] = group["trusted_users"]

            save_groups(groups)

        send_message(
            vk,
            user_id,
            "Пользователь удалён."
        )

        return True

    send_message(
        vk,
        user_id,
        "Неизвестная команда."
    )

    return True