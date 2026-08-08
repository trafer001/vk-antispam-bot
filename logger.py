from datetime import datetime


LOG_FILE = "bot.log"


def log(message):

    now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    text = f"[{now}] {message}"

    print(text)

    try:

        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(text + "\n")

    except Exception as error:

        print(
            f"[{now}] Ошибка записи лога: {error}"
        )
