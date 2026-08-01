from logger import log


def send_message(vk, user_id, text):

    try:

        vk.messages.send(
            user_id=user_id,
            message=text,
            random_id=0
        )

        log(
            f"Отправлено сообщение пользователю {user_id}"
        )

        return True

    except Exception as error:

        log(
            f"Ошибка отправки сообщения: {error}"
        )

        return False