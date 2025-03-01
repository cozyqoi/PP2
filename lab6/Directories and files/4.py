def count_lines(file_path):
    with open(file_path, "r") as file:
        return sum(1 for line in file)

print(count_lines("example.txt"))
