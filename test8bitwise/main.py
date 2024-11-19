can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    check_create = user_permissions & can_create_guild
    return check_create


def get_review_bits(user_permissions):
    check_review = user_permissions & can_review_guild
    return check_review


def get_delete_bits(user_permissions):
    check_delete = user_permissions & can_delete_guild
    return check_delete


def get_edit_bits(user_permissions):
    check_edit = user_permissions & can_edit_guild
    return check_edit

