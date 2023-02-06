def zero_sequence(lst: list) -> bool:
    """
    This function finds out if set include sequence with zero sum of elements.
    @lst: list
    examples: zero_sequence([1, 2, 3, 4, 5, 6]))
         >>> False
         
         zero_sequence([-5, -5, 2, -1,  3, 1, -2]))
         >>> True
    """
    cum_sum_list = [0]
    for i in lst:
        if cum_sum_list[-1] + i in cum_sum_list:
            return True
        else:
            cum_sum_list.append(cum_sum_list[-1] + i )
    return False

