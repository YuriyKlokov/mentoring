from random import random
import timeit

def deco_timer(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        res = func(*args, **kwargs)
        print(f'время выполнения функции составялет {timeit.default_timer() - start_time:.2f} секунд')
        return res
    return wrapper

def main_func(b): 
    cache = {} 
    rnd = random()
    @deco_timer
    def inner_func(c): 
        if c in cache: 
            return sum(cache[c])
        lst2 = []
        for i in range(100000000):
            lst2.append(i * (b + rnd)**(1 / c))
        cache[c] = lst2
        return sum(cache[c])
    return inner_func 

k = main_func(10)
k(12)