def my_combination(digits):
    letters = ['']
    digit_code = {'2': ('a', 'b', 'c'), 
              '3': ('d', 'e', 'f'), 
              '4': ('g', 'h', 'i'),
              '5': ('j', 'k', 'l'), 
              '6': ('m', 'n', 'o'),
              '7': ('p', 'q', 'r', 's'),
              '8': ('t', 'u', 'v'),
              '9': ('w', 'x', 'y', 'z')
             }
    digits = digits.replace('1', '')
    
    if not digits:
        return []
    
    for i in digits:
        additional = []
        for letter_result in letters:
            for add_letter in digit_code[i]:
                additional.append(letter_result + add_letter)
        letters = additional
        
    return letters