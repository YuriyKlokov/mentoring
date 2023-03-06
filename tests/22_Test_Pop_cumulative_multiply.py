from functools import reduce


def pop_cum_multiply(lst: list) -> list:
    """
    This function calculate multiplication of list elements for each element without itself
    @lst: list
    examples: zero_sequence([5, 1, 4, 2]))
         >>> [8, 40, 10, 20]
         # 8 = 1 * 4 * 2
         # 40 = 5 * 4 * 2
         # 10 = 5 * 1 * 2
         # 20 = 5 * 1 * 4
    """
    prev_cum_value = 1
    result = []
    for i in range(len(lst) - 1):
        slice_object = slice(i + 1, None)
        result.append(prev_cum_value * reduce(lambda x, y: x * y, lst[slice_object]))
        prev_cum_value *= lst[i]
    else:
        if len(lst) > 1:
            result.append(prev_cum_value)
    return result


assert [8, 40, 10, 20] == pop_cum_multiply([5, 1, 4, 2]), [5, 1, 4, 2]
assert [8, -40, -10, -20] == pop_cum_multiply([-5, 1, 4, 2]), [5, 1, 4, 2]
assert [0, 0, 0, 20] == pop_cum_multiply([5, 1, 4, 0]), [5, 1, 4, 0]
assert [] == pop_cum_multiply([10]), [10]
assert [] == pop_cum_multiply([]), []
assert [1, 1, 1, 1] == pop_cum_multiply([1, 1, 1, 1]), [1, 1, 1, 1]
assert [0, 0, 0, 0] == pop_cum_multiply([0, 0, 0, 0]), [0, 0, 0, 0]
