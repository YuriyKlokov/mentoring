def my_func(number: int, k: int) -> int:
    """
    This function crosses out the digit in amount of k. The result is the biggest possible number.
    @number = int
    @k = int
    examples: my_func(5167, 1)
         >>> '567'
    """

    int_as_str = list(str(number))
    result = int_as_str[0]
    for i in range(1, len(int_as_str)):
        if len(result) <= len(int_as_str) - k:
            while (
                len(result) > 0
                and result[-1] < int_as_str[i]
                and len(int_as_str) - k - len(result) + 1 <= len(int_as_str) - i
            ):
                result = result[:-1]
        result += int_as_str[i]
    return int(result)
