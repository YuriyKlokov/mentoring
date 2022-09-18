#!/usr/bin/env python
# coding: utf-8

# ### 3. Задача num of same 

# In[8]:


# моё решение
def num_of_same(word: str) -> [int]:
    '''
    This function finds highest number of elements in string that is equal and goes one to each other
    @word: Text
    @return: int
    ------------------
    examples: word = 'aaabbbbcc'
              example = num_of_same(word='aaabbbbcc')
              print(example)
                   (4)
              
    '''
    frst = 0
    global_max = 0   
    for i in range(0, len(word)):
        if i == len(word) - 2 and word[i] != word[i + 1]:
            global_max += 1
        if i < len(word) - 1 and word[i] != word[i + 1]:
            frst = 0
            continue
        frst += 1
        global_max = max(frst, global_max)
        
    print(global_max)


# In[9]:


# эталонное решение
def find_max(string: str) -> int:
    '''
    This function finds highest number of elements in string that is equal and goes one to each other
    @word: Text
    @return: int
    ------------------
    examples: word = 'aaabbbbcc'
              example = num_of_same(word='aaabbbbcc')
              print(example)
                   (4)
              
    '''
    i, j, c_len, max_len = 0, 0, 0, 0,
    while i < len(string):
        if string[j] != string[i]:
            j = i
        max_len = max(max_len, i - j + 1)    
        i += 1
    return max_len


# In[ ]:




