def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

s = "Hello World!"
upper, lower = count_letters(s)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
