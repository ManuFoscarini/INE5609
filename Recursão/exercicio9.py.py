def potencia(n):
    if n <= 1:
        return 1
    else:
        return n**n + potencia(n - 1)


print(potencia(int(input())))