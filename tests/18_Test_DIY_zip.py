def _zip(*args):
    """
    This function is DIY zip() return generator
    @*args: iterable objects
    examples:

             print(list(_zip([-1, -2, -3], 'gd', [4, 5, 6], (10, '234', ' '))))
             >>> [(-1, 'g', 4, 10), (-2, 'd', 5, '234')]

    """

    def inner_gen_func(*args):
        list_of_iter = [iter(x) for x in args]
        example = []
        while True:
            for i in list_of_iter:
                try:
                    example.append(next(i))
                except StopIteration:
                    return
            yield example
            example = []

    result = inner_gen_func(*args)
    for q in result:
        yield (tuple(q))


def g():
    for i in range(1, 5):
        yield i


generator = g()

assert [(-1, "g", 4, 10), (-2, "d", 5, "234")] == list(
    _zip([-1, -2, -3], "gd", [4, 5, 6], (10, "234", " "))
)
assert [] == list(_zip([], "gd", [4, 5, 6], (10, "234", " ")))
assert [(-1, 1), (-2, 2)] == list(_zip([-1, -2], generator))
assert [("h", "w"), ("e", "o"), ("l", "r"), ("l", "l"), ("o", "d")] == list(
    _zip("hello", "world")
)