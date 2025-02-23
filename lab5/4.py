import re

def find_uppercase_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

print(find_uppercase_lowercase("Hello World Python"))  # ['Hello', 'World', 'Python']