def convert_number(roman_number: str) -> int:
    """
    This function convert roman number to arab number.
    @roman_number: str
    @return: int
    ------------------
    examples: num = 'MCMXCIV'
              convert_number(roman_number=num)
              >>>1994
    """
    number_dict = {'I' : 1, 'V' : 5, 'X' :10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    i = len(roman_number)- 1
    result = 0
    while i >= 0:
        if i != 0 and number_dict[roman_number[i]] > number_dict[roman_number[i-1]]:
            result += number_dict[roman_number[i]] - number_dict[roman_number[i-1]]
            i -= 2
        else:
            result += number_dict[roman_number[i]]
            i -= 1
    return result

