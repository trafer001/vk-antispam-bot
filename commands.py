 from logger import log
from sender import send_message
from moderator import is_admin
from config import load_groups, save_groups
from stats import command_used, get_stats


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

    command_used()

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
                "/stats\n"
                "/list\n"
                "/trust ID\n"
                "/untrust ID"
            )
        )

        return True

    if text == "/stats":

        stats = get_stats()

        send_message(
            vk,
            user_id,
            (
                "📊 Статистика\n\n"
                f"Получено сообщений: {stats['received']}\n"
                f"Удалено сообщений: {stats['deleted']}\n"
                f"Команд выполнено: {stats['commands']}"
            )
        )

        return True

    if text == "/list":

        trusted = group.get("trusted_users", [])

        if trusted:

            answer = (
                "👥 Доверенные пользователи:\n\n"
                + "\n".join(
                    str(user)
                    for user in trusted
                )
            )

        else:

            answer = (
                "Список доверенных пользователей пуст."
            )

        send_message(
            vk,
            user_id,
            answer
        )

        return True

    if text.startswith("/trust "):

        parts = text.split()

        if len(parts) != 2:

            send_message(
                vk,
                user_id,
                "Использование: /trust ID"
            )

            return True

        try:

            trusted_id = int(parts[1])

        except ValueError:

            send_message(
                vk,
                user_id,
                "ID пользователя должен быть числом."
            )

            return True

        trusted_users = group.setdefault(
            "trusted_users",
            []
        )

        if trusted_id not in trusted_users:

            trusted_users.append(trusted_id)

            groups = load_groups()

            for item in groups:

                if item.get("group_id") == group.get("group_id"):

                    item["trusted_users"] = list(
                        trusted_users
                    )

                    break

            save_groups(groups)

            send_message(
                vk,
                user_id,
                f"✅ Пользователь {trusted_id} добавлен в доверенные."
            )

        else:

            send_message(
                vk,
                user_id,
                f"Пользователь {trusted_id} уже находится в списке."
            )

        return True

    if text.startswith("/untrust "):

        parts = text.split()

        if len(parts) != 2:

            send_message(
                vk,
                user_id,
                "Использование: /untrust ID"
            )

            return True

        try:

            trusted_id = int(parts[1])

        except ValueError:

            send_message(
                vk,
                user_id,
                "ID пользователя должен быть числом."
            )

            return True

        trusted_users = group.setdefault(
            "trusted_users",
            []
        )

        if trusted_id in trusted_users:

            trusted_users.remove(trusted_id)

            groups = load_groups()

            for item in groups:

                if item.get("group_id") == group.get("group_id"):

                    item["trusted_users"] = list(
                        trusted_users
                    )

                    break

            save_groups(groups)

            send_message(
                vk,
                user_id,
                f"✅ Пользователь {trusted_id} удалён из доверенных."
            )

        else:

            send_message(
                vk,
                user_id,
                f"Пользователя {trusted_id} нет в списке."
            )

        return True

    send_message(
        vk,
        user_id,
        "Неизвестная команда.\nНапишите /help"
    )

    return True
