def is_admin(user_id, group):
    return user_id in group.get("admins", [])


def is_trusted(user_id, group):
    return user_id in group.get("trusted_users", [])


def is_allowed(user_id, group):
    return (
        is_admin(user_id, group)
        or is_trusted(user_id, group)
    )


def get_user_role(user_id, group):

    if is_admin(user_id, group):
        return "admin"

    if is_trusted(user_id, group):
        return "trusted"

    return "member"


def should_delete(user_id, group):
    return get_user_role(user_id, group) == "member"
