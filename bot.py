import json
import os

print("VK AntiSpam Bot запускается...")

# Загружаем настройки групп
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

print("Бот готов к работе")
