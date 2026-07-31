 from config import load_groups

print("=" * 40)
print("VK AntiSpam Bot")
print("=" * 40)

groups = load_groups()

print(f"Найдено групп: {len(groups)}")

for group in groups:

    if not group.get("enabled", True):
        continue

    print(f"✓ {group['name']}")

print("Инициализация завершена")