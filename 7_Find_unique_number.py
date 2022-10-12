def find_unique_number(num_list: [list]) -> int:
    """
    This function finds unique number from list.
    @num_list: list
    @return: int
    ------------------
    examples: lst = [1, 2, 2, 1, 9]
              find_unique_number(num_list=lst)
              >>>9
    """
    num_list.sort()
    i =  0
    while i < len(num_list) - 1:
        if num_list[i] != num_list[i+1]:
            return num_list[i]
        else: 
            i += 2
    return num_list[i]


def find_unique_number(num_list: [list]) -> int:
    """
    This function finds unique number from list.
    @num_list: list
    @return: int
    ------------------
    examples: lst = [1, 2, 2, 1, 9]
              find_unique_number(num_list=lst)
              >>>9
    """
    result = num_list[0]
    for i in range(len(num_list)-1):
        result ^= num_list[i+1]
    return result

