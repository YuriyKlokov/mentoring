from collections import Counter


def find_first_unique_symbol(string: str) -> str:
    """
    This function finds first unique symbol
    @string: str
    examples: string1 = 'abcdcaf'
              find_first_unique_symbol(string1)
              >>>'b'
              string2 = 'fghfghfv'
              find_first_unique_symbol(string2)
              >>>'v'
    """
    for k, v in Counter(string).items():
        if v == 1:
            return k
    return None


assert 'b' == find_first_unique_symbol('abcdcaf'), 'abcdcaf'
assert 'v' == find_first_unique_symbol('fghfghfv')
assert 'b' == find_first_unique_symbol('b'), 'b'
assert  None == find_first_unique_symbol('bb'), 'bb'
assert  None == find_first_unique_symbol(''), ''
assert 'b' == find_first_unique_symbol('abcdcaf1'), 'abcdcaf1'
assert '1' == find_first_unique_symbol('1abcdcaf'), '1abcdcaf'
assert '-' == find_first_unique_symbol('-abcdcaf'), '-abcdcaf'
assert ' ' == find_first_unique_symbol(' abcdcaf'), ' abcdcaf'
assert 'b' == find_first_unique_symbol('aba'), 'aba'
assert 'a' == find_first_unique_symbol('abc'), 'abc'
assert 'b' == find_first_unique_symbol('abaaaaaaaaac'), 'abaaaaaaaaac'
assert 'b' == find_first_unique_symbol('abaaaaaaaaaccc'), 'abaaaaaaaaacccccc'
assert  None == find_first_unique_symbol('bbnnnhhhrrrdddd'), 'bbnnnhhhrrrdddd'