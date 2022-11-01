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

assert 13 == find_max_subtraction([6, 5, 10, 8, 11, 4, 4, 4, 5, 13, 17, 2, 1]), [6, 5, 10, 8, 11, 4, 4, 4, 5, 13, 17, 2, 1] 
assert 4  == find_max_subtraction([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]
assert 6  == find_max_subtraction([2, 2, 3, 1, 7]), [2, 2, 3, 1, 7]
assert 0  == find_max_subtraction([]), [] 
assert 3  == find_max_subtraction([4, 5, 6, 0, 3]), [4, 5, 6, 0, 3]
assert 0  == find_max_subtraction([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1]
assert 0  == find_max_subtraction([10, 9, 8, 7, 6]), [10, 9, 8, 7, 6]
assert 7  == find_max_subtraction([3, 9, 9, 1, 8, 6]), [3, 9, 9, 1, 8, 6]