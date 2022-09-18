#!/usr/bin/env python
# coding: utf-8

# ### 2. Задача sum of two <a id = '2'></a>

# In[2]:


from typing import List, Tuple
def sum_of_two(values: List[int], target: int) -> Tuple[int, int]:
    '''
    This function finds indexes of two list elements which sum equals to target
    @values: List[int>0] 
    @tgarget: int
    @return: Tuple[int, int]
    ------------------
    examples: Lst = [1, 2, 4, 5, 19]
              Trgt = 7
              example = sum_of_two(List = Lst, Target = Trgt)
              print(example)
                   (1, 3)
              
    '''
    seen_el = {}
    for i in range(len(values)):
        dif = target - values[i]
        if dif in seen_el:
            return (i, seen_el[dif])
        seen_el[values[i]] = i   


# In[ ]:




