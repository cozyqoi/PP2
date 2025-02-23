import re

def match_a_anything_b(string):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, string))

print(match_a_anything_b("aXb"))      # True
print(match_a_anything_b("a123b"))    # True
print(match_a_anything_b("a___b"))    # True
print(match_a_anything_b("abX"))      # False