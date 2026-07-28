import json
import os
import vk_api
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")

print("VK AntiSpam Bot запускается...")

if not VK_TOKEN:
    print("Ошибка: токен VK не найден")
    exit()

print("Токен VK найден")

# Подключение к VK
vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

print("Подключение к VK успешно")

# Загружаем группы
with open("groups.json", "r", encoding="utf-8") as file:
    config = json.load(file)

groups = config.get("groups", [])

print(f"Найдено групп: {len(groups)}")

for group in groups:
    print(
        "Группа:",
        group["name"],
        "| ID:",
        group["group_id"]
    )

print("Бот готов")
