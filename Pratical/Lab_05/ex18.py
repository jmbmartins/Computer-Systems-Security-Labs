def mod_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1

def calculate_y(x):
    y = ((22*(x-10)*(x-18)*mod_inverse(10, 23)) + (19*(x-7)*(x-18)*mod_inverse(22, 23)) + (0*(x-7)*(x-10)*mod_inverse(19, 23))) % 23
    return y

valor = calculate_y(0)
print(valor)