def even(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i
            
n = int(input())
arr = []
for i in even(n):
    arr.append(i)
print(arr)    