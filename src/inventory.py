def check_reorder(item):
    if item.quantity <= item.R:
        item.quantity += item.Q
        return True
    return False