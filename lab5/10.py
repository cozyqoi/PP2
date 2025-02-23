import re

def camel_to_snake(string):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', string).lower()

print(camel_to_snake("CamelCaseString"))  # "camel_case_string"