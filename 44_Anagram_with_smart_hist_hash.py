from collections import defaultdict
def find_anagram(input_strings):
    dct = defaultdict(list)
    for i in input_strings:
        hist_hash = [0] * 26
        for j in i:
            hist_hash[ord(j) - ord('a')] += 1
        dct[tuple(hist_hash)].append(i)
    return list(dct.values())
            


print(find_anagram(["eat","tea","tan","ate","nat","bat"]))





