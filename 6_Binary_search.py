def binary_search(list_of_numbers: list, to_found: int) ->int:
    """
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
    """
    end = len(list_of_numbers)
    start = 0
    while start != end:
        middel_index = (start+end)//2
        middel_el = list_of_numbers[middel_index]
        if middel_el < to_found:
            start = middel_index+1
        elif middel_el > to_found: 
            end = middel_index
        else:
            return middel_index
    return -1