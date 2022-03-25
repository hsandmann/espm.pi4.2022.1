def conta_uns(n):
    c = 0
    while n > 0:
        c += 1 if n % 10 == 1 else 0
        n = n // 10
    return c

print(conta_uns(1231231231111171))
