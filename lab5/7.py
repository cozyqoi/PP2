import re

def snake_to_camel(string):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), string)

print(snake_to_camel("snake_case_string"))  # "snakeCaseString"