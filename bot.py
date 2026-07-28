import json
import os
import vk_api
from vk_api.longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")

print("VK AntiSpam Bot запускается...")

if not VK_TOKEN:
    print("Ошибка: токен VK не найден")
    exit()

vk_session = vk_api.VkApi(token=VK_TOKEN)

vk = vk_session.get_api()

with open("groups.json", "r", encoding="utf-8") as file:
    config = json.load(file)

groups = config.get("groups", [])

print(f"Групп загружено: {len(groups)}")


# Пока тестируем первую группу
group = groups[0]

group_id = group["group_id"]

print("Подключаем группу:", group["name"])


longpoll = VkBotLongPoll(
    vk_session,
    group_id
)

print("Бот слушает сообщения...")


for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:

        user_id = event.object.message["from_id"]

        text = event.object.message["text"]

        print(
            "Новое сообщение:",
            user_id,
            text
        )
