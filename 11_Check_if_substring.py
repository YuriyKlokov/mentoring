def check_if_substring(substring: str, word: str) -> bool:
    """
    This function check if word contains substring
    
    @substring: str
    @word: str
    @return: bool
    examples: substring = 'abc'
              word  = 'ahbgdc'
              check_if_substring(substring, word)
              >>>True
    """
    i = 0
    result = False
    while len(word) > i:
        if word[i] == substring[0]:
            substring = substring[1:]
        i += 1
    print(len(substring) == 0)