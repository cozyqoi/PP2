import re

def find_lowercase_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

print(find_lowercase_underscore("hello_world abc_def"))  # ['hello_world', 'abc_def']