def find_min_subtraction(first_list, second_list):
    
    """
    This function finds minimum absolute subtraction between elemnts of two list.
    
    @first_list: list
    @second_list: list
    examples: lst1 = [1, 2, 7, 50]
              lst2  = [-1, 11, 12, 13, 8]
              find_min_subtraction(first_list=lst1, second_list=lst2)
              >>>(7, 8)
    """

    min_one, min_two = None, None 
    i, j  = 0, 0
    min_num = float('inf')
    first_list.sort()
    second_list.sort()
    while i < len(first_list) and  j < len(second_list):
        if  abs(first_list[i] - second_list[j]) <= min_num :
            min_one = first_list[i]
            min_two = second_list[j] 
            min_num = abs(first_list[i] - second_list[j])
        if first_list[i] < second_list[j]:
            i += 1
        else:
            first_list[i] > second_list[j]
            j += 1         
    return (min_one, min_two)

assert (7, 8) == find_min_subtraction([1, 2, 7, 50], [-1, 11, 12, 13, 8]), ([1, 2, 7, 50], [-1, 11, 12, 13, 8])
assert (None, None) == find_min_subtraction([], [-1, 11, 12, 13, 8]), ([], [-1, 11, 12, 13, 8])
assert (None, None) == find_min_subtraction([1, 2, 7, 50], []), ([1, 2, 7, 50], [])
assert (None, None) == find_min_subtraction([], []), ([], [])
assert (1, 10) == find_min_subtraction([1], [10]), ([1], [10])
assert (1, 10) == find_min_subtraction([1, 1, 1], [10, 10, 10]), ([1, 1, 1], [10, 10, 10])
assert (8, 10) == find_min_subtraction([1, 8, 1], [10, 10, 10]), ([1, 8, 1], [10, 10, 10])
assert (8, 8) == find_min_subtraction([1, 8, 1], [10, 8, 10]), ([1, 8, 1], [10, 8, 10])
assert (8, 8) == find_min_subtraction([1, 8, 1], [10, 8, 10]), ([1, 8, 1], [10, 8, 10])
assert (-8, -10) == find_min_subtraction([-1, -8, -1], [-10, 10, -10]), ([-1, -8, -1], [-10, 10, -10])
assert (-8, -8) == find_min_subtraction([-1, -8, -1], [-10, -8, -10]), ([-1, -8, -1], [-10, -10, -10])
assert (1, -1) == find_min_subtraction([1, 2, 49, 50], [-1, 11, 12, 13, 8]), ([1, 2, 49, 50], [-1, 11, 12, 13, 8])



