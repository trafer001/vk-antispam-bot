from logger import log


def delete_message(vk, group, message_id):

    try:

        vk.messages.delete(
            message_ids=message_id,
            delete_for_all=1
        )

        log(
            f"[{group['name']}] "
            f"Сообщение {message_id} удалено"
        )

        return True

    except Exception as error:

        log(
            f"[{group['name']}] "
            f"Ошибка удаления: {error}"
        )

        return False
