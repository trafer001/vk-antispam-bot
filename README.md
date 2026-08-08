# VK AntiSpam Bot

Бот-модератор для сообществ VK.

## Возможности

- подключение нескольких групп VK;
- работа через VK Bot Long Poll;
- определение ролей пользователей;
- администраторы;
- доверенные пользователи;
- автоматическая обработка сообщений;
- удаление сообщений пользователей, не входящих в разрешённые списки;
- команды администратора;
- логирование событий;
- запуск нескольких групп одновременно.

## Структура проекта

```text
bot.py
commands.py
config.py
delete_message.py
logger.py
main.py
moderator.py
sender.py
vk_client.py

groups.example.json
requirements.txt
README.md
.gitignore
