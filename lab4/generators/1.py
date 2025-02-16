def square(N):
    for i in range(N+1):
        yield i*i

n = int(input())
for i in square(n):
    print(i)