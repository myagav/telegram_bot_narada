from config import ADMINS


def is_admin(user_id: int):
    if user_id in ADMINS:
        return True
    else:
        return False
