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


assert [2, 0, 3] == list_digits_add([1, 2, 3], [8, 0]), "[1, 2, 3], [8, 0]"
assert [8] == list_digits_add([], [8]), "[], [8]"
assert [] == list_digits_add([], []), "[], []"
assert [1, 1] == list_digits_add([5], [6]), "[5], [6]"
assert [5] == list_digits_add([5], [0]), "[5], [0]"
assert [1, 0, 0, 0] == list_digits_add([8, 0, 0], [2, 0, 0]), "[5, 0, 0], [2, 0, 0]"
assert [4, 4, 4] == list_digits_add([1, 2, 3], [3, 2, 1]), "[5, 0, 0], [2, 0, 0]"