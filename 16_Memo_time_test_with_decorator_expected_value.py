from random import random
from numpy import average
import timeit


def deco__time_expected_value(number_of_start):
    def deco_timer(func):
        def wrapper(*args, **kwargs):
            list_of_values = []
            nonlocal number_of_start
            while number_of_start - 1 >= 0:
                start_time = timeit.default_timer()
                res = func(*args, **kwargs)
                number_of_start -= 1
                list_of_values.append(timeit.default_timer() - start_time)
            return f"выборочное мат. ожидание времени выполнения функции составляет: {average(list_of_values)} секунд"

        return wrapper

    return deco_timer


def main_func(b):
    cache = {}
    rnd = random()

    @deco__time_expected_value(30)
    def inner_func(c):
        if c in cache:
            return sum(cache[c])
        lst2 = []
        for i in range(100000000):
            lst2.append(i * (b + rnd) ** (1 / c))
        cache[c] = lst2
        return sum(cache[c])

    return inner_func


k = main_func(10)
k(56)
