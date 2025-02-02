lst = input("elementer engiz: ").split()
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print("unique elementter:", unique)