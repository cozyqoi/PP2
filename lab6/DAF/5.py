items = ["apple", "banana", "cherry"]

with open("fruits.txt", "w") as file:
    for item in items:
        file.write(item + "\n")
