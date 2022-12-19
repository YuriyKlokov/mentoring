def _zip(*args):
    
    """
    This function is DIY zip() return generator
    @*args: iterable objects
    examples:
             
             print(list(_zip([-1, -2, -3], 'gd', [4, 5, 6], (10, '234', ' '))))
             >>> [(-1, 'g', 4, 10), (-2, 'd', 5, '234')]
    
    """
    
    def inner_gen_func(*args):
        list_of_iter = [iter(x) for x in args]
        example = []
        while True :
            for i in list_of_iter:
                try:
                    example.append(next(i))
                except StopIteration:
                    return 
            yield example
            example = []
            
    result = inner_gen_func(*args)
    for q in result:
        yield (tuple(q))