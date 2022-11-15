def find_type_of_list(numbers: list) -> bool:
    """
    This function define if  list is monotonic
    @numbers: list
    examples: numbers = [4, 4, 4, 3, 2, 19]
              find_type_of_list([4, 4, 4, 3, 2, 19])
              >>>False
              numbers = [5, 4, 3, 2]
              find_type_of_list([4, 4, 4, 3, 2, 19])
              >>>True
    """
    signal, i  = 0, 0 
    mark = True
    
    if len(numbers)> 0 and numbers[0] > numbers[-1]  :# убывает
        signal = -1      
    elif len(numbers)> 0 and numbers[0] < numbers[-1]:
        signal = 1  # возрастает
    else:
        signal = 0
        
    while mark == True and i < len(numbers)-1: 
        if signal == 0 and max(numbers) == min(numbers):
            i += len(numbers)
        if (signal == 1 and numbers[i] > numbers[i+1]) or (signal == -1 and numbers[i] < numbers[i+1] 
                                                           or (signal == 0 and max(numbers) != min(numbers))):
            mark = False
        i += 1
    return mark

assert False == find_type_of_list([4, 4, 4, 3, 2, 19]), [4, 4, 4, 3, 2, 19]
assert True == find_type_of_list([5, 4, 3, 2]), [5, 4, 3, 2]
assert True == find_type_of_list([1, 2, 3, 4]), [1, 2, 3, 4]
assert True == find_type_of_list([1, 1, 1, 1]), [1, 1, 1, 1]
assert True == find_type_of_list([1, 1]), [1, 1]
assert True == find_type_of_list([1, 2]), [1, 2]
assert True == find_type_of_list([2, 1]), [2, 1]
assert True == find_type_of_list([]), []
assert False == find_type_of_list([34, 63, 78, 3, 643]), [34, 63, 78, 3, 643]
assert False == find_type_of_list([1, 63, 1]), [1, 63, 1]
assert False == find_type_of_list([63, 1, 63]), [63, 1, 63]