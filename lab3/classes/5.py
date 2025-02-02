def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

numbers = list(map(int, input("sandar engiz: ").split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("zhai sandar:", prime_numbers)