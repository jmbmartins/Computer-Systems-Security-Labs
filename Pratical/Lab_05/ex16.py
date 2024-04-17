def calculate_y(x):
    y = (1 + 6*x + 19*(x**2) + 14*(x**3)) % 23
    return y


y = calculate_y(7)
print(f"O valor de y é {y}")