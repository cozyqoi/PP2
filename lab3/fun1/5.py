from itertools import permutations

s = input("engiz: ")
perms = [''.join(p) for p in permutations(s)]
print("all permutations:", perms)