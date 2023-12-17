from random import random
from typing import Any, Iterable 
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
def my_r_sampling(k: int, iter_odj: Iterable) -> list:
    r_list = []
    for i, el in enumerate(iter_odj):
        if i + 1 <= k:
            r_list.append(el)
        else:
            j = int(random() * i)
            if  j <= k - 1:
                r_list[j] = el
    return r_list
            
    
def generator(max):
    number = 1
    while number < max:
        number += 1
        yield number
        
        
dct = defaultdict(int)
for i in range(1000000):
    my_generator = generator(10)
    examp = my_r_sampling(5, my_generator)
    result_str = ''.join(map(lambda x: str(x)+' ', examp))
    dct[result_str] += 1
    
labels = list(dct.keys())
values = list(dct.values())
plt.bar(labels, values)





