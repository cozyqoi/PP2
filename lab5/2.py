import re

def match_ab_two_three(string):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, string))

print(match_ab_two_three("abb"))    # True
print(match_ab_two_three("abbb"))   # True
print(match_ab_two_three("ab"))     # False
print(match_ab_two_three("abbbb"))  # False