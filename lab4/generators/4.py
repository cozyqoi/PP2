def square(a, b):
    for i in range(a, b + 1):
        yield i * i

n = int(input())
m = int(input())   
for i in square(n, m):
    print(i)     