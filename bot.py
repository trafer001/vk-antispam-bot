import json
import os
from dotenv import load_dotenv

load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")

print("VK AntiSpam Bot запускается...")

if VK_TOKEN:
    print("Токен VK найден")
else:
    print("Ошибка: токен VK не найден")

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

print("Настройки загружены")
