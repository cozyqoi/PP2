def div(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for i in div(n):
    print(i)            