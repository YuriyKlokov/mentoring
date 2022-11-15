from random import random
import timeit

def main_func(b): 
    cache = {} 
    rnd = random() 
    def inner_func(c): 
        if c in cache: 
            return sum(cache[c])
        lst2 = []
        for i in range(100000000):
            lst2.append(i * (b + rnd)**(1 / c))
        cache[c] = lst2
        return sum(cache[c])
    return inner_func 
k = main_func(100) 

start_time = timeit.default_timer() 
k(2)
diff1 = timeit.default_timer() - start_time
print() 
start_time = timeit.default_timer() 
k(2)
diff2 = timeit.default_timer() - start_time
print('первый запуск {:.2f} секунд'.format(diff1))
print('второй запуск {:.2f} секунд'.format(diff2))
print('второй быстрее в {:.1f} раза'.format(diff1/diff2))




