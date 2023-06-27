def find_max_multi(lst: list) -> list:
    """
    This function retrun two numbers in list with max multiply resilt

    @lst: list
    @return: list
    ------------------
    examples: find_max_multi([11, 18, -9, -30])
              >>>[-30, -9]
    """
    max_pozitive_one = 0
    max_pozitive_two = 0
    min_negative_one = float("inf")
    min_negative_two = float("inf")
    for i in lst:
        if i > max_pozitive_one:
            max_pozitive_two = max_pozitive_one
            max_pozitive_one = i
        elif i > max_pozitive_two:
            max_pozitive_two = i
        elif i < 0 and i < min_negative_one:
            min_negative_two = min_negative_one
            min_negative_one = i
        elif i < min_negative_two:
            min_negative_two = i
    return max(
        [max_pozitive_one, max_pozitive_two],
        [min_negative_one, min_negative_two],
        key=lambda x: sum(x) * -1,
    )