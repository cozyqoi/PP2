import re

def match_ab(string):
    pattern = r'ab*'
    return bool(re.fullmatch(pattern, string))

print(match_ab("a"))     # True
print(match_ab("ab"))    # True
print(match_ab("abb"))   # True
print(match_ab("ac"))    # False