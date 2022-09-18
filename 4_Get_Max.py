#!/usr/bin/env python
# coding: utf-8

# ### 4. Задача Get max

# In[8]:


lst_salary =  [('Юра', 1000), ('Андрей', 500), ('Кринж', 2000)]


# In[11]:


# моё решение

from typing import List, Text, Tuple
def max_salary(lst_salary):
    '''
    This function finds max salary tuple from list of tuples  
    @lst_salary: List
    @return: Tuple
    ------------------
    examples: lst_salary = [('Юра', 1000), ('Андрей', 500), ('Кринж', 2000)]
              example = max_salary(lst_salary)
              print(example)
                   ('Кринж', 2000)
              
    '''
    max_tuple = (0, 0)
    for i in lst_salary: 
        if i[1] > max_tuple[1]:
            max_tuple = i
    return max_tuple


# In[12]:


# эталонное решение
print(max(lst_salary, key=lambda x: x[1]))


# In[15]:


#вывод индекса максимального кортежа
print(lst_salary.index(max(lst_salary, key=lambda x: x[1])))

[index for index in range(len(lst_salary)) if lst_salary[index] == max(lst_salary, key=lambda x: x[1])][0]


# In[ ]:




