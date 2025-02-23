import re

def insert_spaces(string):
    return re.sub(r'([A-Z])', r' \1', string).strip()

print(insert_spaces("CamelCaseString"))  # "Camel Case String"