#!/usr/bin/env python
# coding: utf-8

# ### 1. Задача polyndrome_num

# In[9]:


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


# In[10]:


assert True == polyndrome_num(0), 0
assert True == polyndrome_num(1), 1
assert True == polyndrome_num(11), 11
assert True == polyndrome_num(111), 11
assert True == polyndrome_num(121), 121
assert True == polyndrome_num(1221), 1221
assert False == polyndrome_num(10), 10
assert False == polyndrome_num(1234), 1234


# In[ ]:





# In[ ]:




