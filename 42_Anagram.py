from collections import defaultdict
def find_anagram(input_strings):
    dct = defaultdict(list)
    for i in input_strings:
        key = ''.join(sorted(i))
        dct[key].append(i)
    return list(dct.values())


print(find_anagram(["eat","tea","tan","ate","nat","bat"]))


