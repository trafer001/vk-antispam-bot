stats = {
    "received": 0,
    "deleted": 0,
    "commands": 0
}


def message_received():
    stats["received"] += 1


def message_deleted():
    stats["deleted"] += 1


def command_used():
    stats["commands"] += 1


def get_stats():
    return stats.copy()