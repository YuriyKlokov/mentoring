def yandex_funny_soundex(word: str) -> str:
    """
    This function carry out soundex algorithm. This algorithm finds out if words sounds similar.
    Function returns 4 digit code. 
    @word:  word
    ------------------
    examples: yandex_funny_soundex('ammonium')
              a500
    
    """    
    
    number_dict = {'a': '0', 'e': '0', 'h': '0', 'i': '0', 'o': '0', 'u': '0', 'w': '0', 'y': '0',
                   'b': '1', 'f': '1', 'p': '1', 'v': '1',
                   'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
                   'd': '3', 't': '3',
                   'l': '4',
                   'm': '5', 'n': '5',
                   'r': '5'
                 }
        
    result = word[0]
    for i in range(1, len(word)):
        if number_dict[word[i]] == '0' or number_dict[word[i]] == result[-1]:
            continue
        result += number_dict[word[i]]
    
    if len(result)<= 4:
        result = result + '0'* (4 - len(result))
    else:
        result = result[:4]
    
    print(result)    
        

