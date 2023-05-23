def list_digits_add(lst1: list, lst2: list) -> list:
    """
    This function adds two numbers that are represented as list of digits
    @lst1: list
    @lst2: list
    @return: list
    ------------------
    examples: lst1 = [1, 2, 3]
              lst2 = [8, 0]
              list_digits_add(lst1, lst2)
              >>> [2, 0, 3]
    """
    max_len = max(len(lst1), len(lst2))
    min_len = min(len(lst1), len(lst2))
    max_list = []
    min_list = []
    if len(lst1) == max_len:
        max_list = lst1
        min_list = lst2
    else:
        max_list = lst2
        min_list = lst1
    for i in range(-1, -min_len - 1, -1):
        dec, num = divmod(max_list[i] + min_list[i], 10)
        max_list.insert(i, num)
        max_list.pop(i)
        if dec == 1:
            if -i == max_len:
                max_list.insert(i - 1, 1)
            else:
                max_list[i - 1] = max_list[i - 1] + 1
    return max_list




