import re

def replace_space_comma_dot(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

print(replace_space_comma_dot("Hello, world. Python"))  # "Hello::world::Python"