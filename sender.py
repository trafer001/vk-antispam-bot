from logger import log


def send_message(vk, user_id, text):

    try:

        vk.messages.send(
            user_id=user_id,
            random_id=0,
            message=text
        )

        log(f"Отправлено сообщение пользователю {user_id}")

    except Exception as error:

        log(f"Ошибка отправки сообщения: {error}")