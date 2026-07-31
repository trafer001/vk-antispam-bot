def is_admin(user_id, group):
    return user_id in group.get("admins", [])


def is_trusted(user_id, group):
    return user_id in group.get("trusted_users", [])



def should_delete(user_id, group):

    if is_admin(user_id, group):
        return False

    if is_trusted(user_id, group):
        return False

    return True