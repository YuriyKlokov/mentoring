def polyndrome_num(num: int) -> bool:
    '''
    This finction checks if given number is polyndrome or not, and returns True if it does.
        @num: int
    @return: str
    ------------------
    examples: num = 1221
              polyndrome_num(num=1221)
              >>>True 
    '''
    quotient = num
    revers_num = 0 
    while(quotient > 0):
        quotient, remainder = divmod(quotient, 10)
        revers_num = revers_num * 10 + remainder
    if revers_num == num:
        return  True 
    else: return False

