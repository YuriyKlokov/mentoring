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