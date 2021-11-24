def check_list(arg1: list, arg2: int) -> bool:
    if arg2 in arg1:
        return True
    else:
        return False


print(check_list([1, 2, 3, 4, 5], 8))
