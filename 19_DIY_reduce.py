def DYI_reduce(func, obj, start=None):
    """
    This function is DIY reduce() function from functools
    @func: Callable function with two arguments. 
           this function is need to cumulatively apply 
           to arguments of the sequence
    @obj: iteriable object
    @start: item which will be put before first item of  sequence
    
    examples: DYI_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
             >>> 15
    
    """
    
    inter_obj = iter(obj)
    if start != None:
        first_element = start
    else:
        first_element = next(inter_obj)
    for i in inter_obj:
        first_element = func(first_element, i)
    return first_element
