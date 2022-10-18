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
    dct = {}
    for i in range(len(word)):
        if word[i] in dct:
            dct[word[i]] += 1
        else: dct[word[i]] = 1
    odd_count = 0
    max_odd = 0
    result = 0
    for key in dct.keys():
        if dct[key] > 1 and dct[key] % 2 == 1:
            if dct[key] == max(dct.values()):
                max_odd = dct[key]
                odd_count = 1 
            else:
                result += dct[key] - 1
                odd_count = 1 
        elif dct[key] % 2 == 0:
            result += dct[key]
    if odd_count == 0 and result != len(word):
        result += 1
    return result + max_odd

