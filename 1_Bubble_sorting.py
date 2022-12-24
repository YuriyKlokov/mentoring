def bubble_sort(values: [], tip=['desc', 'asc']) -> []:
    
    '''
    This function carries out bubble sroting 
    @values: [] 
    @tip = ['desc', 'asc']
    @[]
    ------------------
    examples: val_lst = [1, 23, 4, 2, 19]
              example = bubble_sort(values=val_lst, tip=desc)
              print(example)
                   (23, 19, 4, 2, 1)
                   
              example = bubble_sort(values=val_lst, tip=asc)
              print(example)
                   (1, 2, 4, 19, 23)              
    '''
    
    for k in range(0, len(values) - 1):
        for i in range(0, len(values) - 1 - k):
            if (tip == 'asc' and values[i] > values[i + 1]):
                values[i] , lst[i + 1] = values[i + 1] , values[i]
            elif (tip == 'desc' and values[i] < values[i + 1]):
                values[i] , values[i + 1] = values[i + 1] , values[i]
    return values