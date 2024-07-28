def is_id_valid(user_data):
    last_char = user_data['id'][-1]
    if last_char.isdecimal():
        return True
    else:
        return False