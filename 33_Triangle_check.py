def triangle_check(a, b, c): 
    if a + b > c and b + c > a and a + c > b:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return True 
        else: return False
    else: return False
