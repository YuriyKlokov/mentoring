def pop_cum_multiply(lst:list, backwards=False) -> list:
    """
    This function calculate multiplication of list elements for each element without itself
    Also you can chane the direction using backwards. direction fro left to right is default.
    @lst: list
    examples: zero_sequence([5, 1, 4, 2]))
         >>> [8, 40, 10, 20]
         # 8 = 1 * 4 * 2
         # 40 = 5 * 4 * 2
         # 10 = 5 * 1 * 2
         # 20 = 5 * 1 * 4
    """
    forward = 1
    backward = 1
    result = []
    if len(lst) < 2:
        return result
    forward_list = [forward := forward * i for i in lst]
    backward_list = [backward := backward * i for i in lst[::-1]]
    forward_list.insert(0, 1)
    backward_list.insert(0, 1)
    for i in range(0, len(lst)):
        result.append(forward_list[i] * backward_list[-i - 2])
    if backwards == True: 
        return result[::-1]
    return result


assert [8, 40, 10, 20] == pop_cum_multiply([5, 1, 4, 2]) , [5, 1, 4, 2]
assert [20, 10, 40, 8] == pop_cum_multiply([5, 1, 4, 2], True) , [5, 1, 4, 2]
assert [8, -40, -10, -20] == pop_cum_multiply([-5, 1, 4, 2]) , [5, 1, 4, 2]
assert [0, 0, 0, 20] == pop_cum_multiply([5, 1, 4, 0]) , [5, 1, 4, 0]
assert [] == pop_cum_multiply([10]) , [10]
assert [] == pop_cum_multiply([]) , []
assert [1, 1, 1, 1] == pop_cum_multiply([1, 1, 1, 1]) , [1, 1, 1, 1]
assert [0, 0, 0, 0] == pop_cum_multiply([0, 0, 0, 0]) , [0, 0, 0, 0]

