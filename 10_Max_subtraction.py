def find_max_subtraction(lst: list) -> int:
    """
    This function find max subtraction.
    index of minuend should be less then index of difference
    subtraction cannot be less than 0 
    
    @lst: list
    @return: int
    ------------------
    examples: lst_of_num = [6, 5, 10, 8, 11, 4, 4, 4, 5, 13, 17, 2, 1]
              find_max_subtraction(lst=lst_of_num)
              >>>13
    """
    delta = 0
    min_num = float('inf')
    for i in range(len(lst)):
        if lst[i] <= min_num:
            min_num = lst[i]
        else: 
            delta = max(lst[i] - min_num, delta)
    return delta