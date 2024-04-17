def lagrange_interpolation(x, w, mod):
    total = 0
    for i in range(len(w)):
        xi, yi = w[i]
        def g(i, acc):
            for j in range(len(w)):
                if i != j:
                    xj, yj = w[j]
                    acc = acc * (x - xj) * mod_inverse(xi - xj, mod) % mod
            return acc
        total += g(i, yi)
        total %= mod
    return total

def mod_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1

shares = [(7, 15), (12, 16), (17, 9)]
x = 0
mod = 23
secret = lagrange_interpolation(x, shares, mod)
print(f"O número de Bitcoins que o grupo de amigos comprou na sua juventude é {secret}")