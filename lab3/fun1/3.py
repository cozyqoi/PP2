def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return (chickens, rabbits)
    return "NO"

heads = int(input("bas sany: "))
legs = int(input("ayak sany: "))
result = solve(heads, legs)
if isinstance(result, tuple):
    print("Tauyk:", result[0], ", Koyan:", result[1])
else:
    print(result)