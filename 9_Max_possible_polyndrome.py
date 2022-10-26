from collections import Counter

def find_max_possible_polyndrome(word: str) -> int:
    """
    This function return lenght of max possible polyndrome that is made from given word
    @word: str
    @return: int
    ------------------
    examples: exp_word  =  ''faaffffanmklllllll''
              find_max_possible_polyndrome(word=exp_word)
              >>>13
    """
    dct = Counter(word)
    odd_count = 0
    max_odd = 0
    result = 0
    for i in dct:
        if dct[i] > 1 and dct[i] % 2 == 1:
            if dct[i] == dct[max(dct, key=lambda x: dct[x])]:
                max_odd = dct[i]
                odd_count = 1     
            elif dct[max(dct, key=lambda x: dct[x])] % 2 == 0:
                result += dct[i] 
                odd_count = 1 
            else:
                result += dct[i] - 1
                odd_count = 1 
        elif dct[i] % 2 == 0:
            result += dct[i]
    if odd_count == 0 and result != len(word):
        result += 1
    return result + max_odd

