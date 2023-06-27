def find_max(number, k):
    '''
    This function crosses out the digit in amount of k. The result is the biggest possible number.
    @number = int
    @k = int
    examples: my_func(5167, 1)
         >>> '567'
    '''
    
    int_as_str = list(str(number))
    end_point = len(int_as_str) - k 
    result = [int_as_str[0]]
    if end_point == 0:
        return []
    for i in range(1, len(int_as_str)):
        if len(result) < len(int_as_str) - k: 
            while (
                len(result) > 0
                and result[-1] < int_as_str[i]
                and end_point - len(result) + 1 <= len(int_as_str) - i
            ):
                result.pop()
            result.append(int_as_str[i])
        else:
            while (
                len(result) > 0
                and result[-1] < int_as_str[i]
                and end_point - len(result) + 1 <= len(int_as_str) - i
            ):
                result.pop()
                result.append(int_as_str[i])
    return result

