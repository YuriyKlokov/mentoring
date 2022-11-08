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




