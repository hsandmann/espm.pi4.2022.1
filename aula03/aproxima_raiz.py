def raiz(n):
    impar = 1
    r = 0
    while n > 0:
        n = n - impar
        impar += 2
        r += 1
    return r

print(raiz(49))
