def check_value(data):
    if isinstance(data, int) or isinstance(data, float):
        if data <= 0:
            return False
    elif isinstance(data, str) or isinstance(data, list):
        return False
    return True