def find_max_subtraction(lst: list) -> int:
    """
    This function find max subtraction.
    index of minuend should be less then index of difference
    subtraction cannot be less than 0 
    
    @lst: list
    @return: int
    ------------------
    examples: lst_of_num = [6, 5, 10, 8, 11, 4, 4, 4, 5, 13, 17, 2, 1]
              find_max_subtraction(lst=lst_of_num)
              >>>13
    """
    fisrt_mark = -1
    switcher = 0
    min_num, min_num2, max_num, max_num2 = 0, 0, 0, 0
    delta, delta2 = 0, 0 
    for i in range(0, len(lst) - 1):
        if lst[i + 1] - lst[i] > 0:
            if fisrt_mark == -1:
                min_num, max_num = lst[i], lst[i + 1]
                delta = lst[i + 1] - lst[i]
                fisrt_mark = 0
            elif lst[i + 1] > max_num and switcher == 0:
                delta += lst[i + 1] - max_num
                max_num = lst[i + 1]
            elif lst[i + 1] > max_num2 and switcher == 1:
                delta2  += lst[i + 1] - max_num2
                max_num2 = lst[i + 1]    
                if delta2 > delta:
                    delta = delta2
                    min_num, max_num = min_num2, max_num2
                    min_num2, max_num2, switcher, delta2 = 0, 0, 0, 0
        elif lst[i] > lst[i + 1] and lst[i + 1] < min_num:
            max_num2, min_num2  = lst[i + 1], lst[i]
            switcher = 1
    return delta  

