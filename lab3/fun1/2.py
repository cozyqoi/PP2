def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

f = float(input("temperature F: "))
print(f, "°F =", round(fahrenheit_to_celsius(f), 1), "°C")