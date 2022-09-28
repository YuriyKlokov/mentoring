def binary_search(list_of_numbers: list, to_found: int) ->int:
    '''
    This function carry out binary search
    @list_of_numbers: list[int]
    @to_found: int
    @return: int
    ------------------
    examples: lst = [1, 2, 4, 5, 19]
              trgt = 2
              example = binary_search(list_of_numbers=lst, to_found=trgt)
              print(example)
              >>>1
    '''
    length = len(list_of_numbers)
    end = length - 1
    start = 0
    middel_index = (start + end) // 2
    middel_el = list_of_numbers[middel_index]
    mark = 0
    while mark == 0:
        if start == end:
            if mid_element != to_search:
                mark = -1      
        elif middel_el > to_found:
            end = middel_index - 1
            middel_index = (start + end) // 2
            middel_el = list_of_numbers[middel_index]
            if middel_el == to_found:
                return middel_index
        elif middel_el < to_found:
            start = middel_index + 1
            end = length - 1
            middel_index = (start + end) // 2
            middel_el = list_of_numbers[middel_index]
            if middel_el == to_found:
                return middel_index
        elif middel_el == to_found:
            return middel_index