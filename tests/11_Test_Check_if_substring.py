def check_if_substring(substring: str, word: str) -> bool:
   """
   This function check if word contains substring
   
   @substring: str
   @word: str
   @return: bool
   examples: substring = ''abc''
             word  = ''ahbgdc''
             check_if_substring(substring, word)
             >>>True
   """
   i = 0
   k = 0
   result = False
   while len(word) > i:
       if substring and k < len(substring) and word[i] == substring[k]:
           k += 1
       i += 1
   return k == len(substring)

assert True  == check_if_substring('abc', 'ahbgdc'), ('abc', 'ahbgdc')
assert False == check_if_substring('acb', 'ahbgdc'), ('acb', 'ahbgdc')
assert True  == check_if_substring('a', 'ahbgdc'), ('a', 'ahbgdc')
assert True  == check_if_substring('', 'ahbgdc'), ('', 'ahbgdc')
assert False == check_if_substring('ahbgdc', ''), ('ahbgdc', '')
assert True  == check_if_substring('', ''), ('', '')
assert False == check_if_substring('fgh', 'asd'), ('fgh', 'asd')
assert True  == check_if_substring('d', 'asd'), ('d', 'asd')
assert True  == check_if_substring('s', 'asd'), ('s', 'asd')
assert True  == check_if_substring('abc', 'ahcbgdc'), ('abc', 'ahcbgdc')
assert True  == check_if_substring('tt', 'ahtbgdtc'), ('tt', 'ahtbgdtc')