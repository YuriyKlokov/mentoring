def zero_sequence(lst: list) -> bool:
    """
    This function finds out if set include sequence with zero sum of elements.
    @lst: list
    examples: zero_sequence([1, 2, 3, 4, 5, 6]))
         >>> False
         
         zero_sequence([-5, -5, 2, 3, -2]))
         >>> True
    """
    cum_sum_list = [0]
    for i in lst:
        if cum_sum_list[-1] + i in cum_sum_list:
            return True
        else:
            cum_sum_list.append(cum_sum_list[-1] + i )
    return False


assert True == zero_sequence([0]) , [0]
assert True == zero_sequence([1, 0, 10]), [1, 0, 10]
assert True == zero_sequence([11, 0, 10]), [11, 0, 10]
assert True == zero_sequence([11, 10, -5, -5, 3, 4]), [11, 10, -5, -5, 3, 4]
assert True == zero_sequence([1, -1, 3]), [1, -1, 3]
assert True == zero_sequence([-5, -5, 2, 3, -2]), [-5, -5, 2, 3, -2]
assert False == zero_sequence([11, 10, 3, 4]), [11, 10, 3, 4]
assert False == zero_sequence([-1, -1, 10, 1]), [-1, -1, 10, 1]
assert False == zero_sequence([]), []
assert False == zero_sequence([1, 2, 2, 4, -1]), [1, 2, 2, 4, -1]
assert False == zero_sequence([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6]
