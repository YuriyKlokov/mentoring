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
            if dct[i] == dct[max(dct, key=lambda x: dct[x] if dct[x] % 2 == 1 else False)] and odd_count == 0:
                max_odd = dct[i]
                odd_count = +1     
            else:
                result += dct[i] - 1
        elif dct[i] % 2 == 0:
            result += dct[i]
    if odd_count == 0 and result != len(word):
        result += 1
    return result + max_odd

assert 13 == find_max_possible_polyndrome('faaffffanmklllllll'), 'faaffffanmklllllll'
assert 1  == find_max_possible_polyndrome('f'), 'f' 
assert 1  == find_max_possible_polyndrome('fa'),'fa'
assert 0  == find_max_possible_polyndrome(''), ''
assert 1  == find_max_possible_polyndrome('asd'), 'asd'
assert 5  == find_max_possible_polyndrome('aassd'), 'aassd'
assert 3  == find_max_possible_polyndrome('ssd'), 'ssd'
assert 5  == find_max_possible_polyndrome('mmmkjjj'), 'mmmkjjj'
assert 9  == find_max_possible_polyndrome('mmmjjjkkkk'), 'mmmjjjkkkk'
assert 9  == find_max_possible_polyndrome('mmjjjkkkk'), 'mmjjjkkkk'
assert 10 == find_max_possible_polyndrome('mmjjjjkkkk'), 'mmjjjjkkkk'
assert 55 == find_max_possible_polyndrome('zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez'), 'zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez'
assert 983 ==  find_max_possible_polyndrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'), 'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'