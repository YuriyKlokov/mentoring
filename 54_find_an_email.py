import re

def check_is_email(word):
    pattern = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if pattern.match(word):
        print('THIS IS AN EMAIL')
    else:
        print('THIS IS NOT AN EMAIL')