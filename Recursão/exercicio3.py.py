def recursao(n):
    if n <= 0:
        return 0
    else:
        return str(n) + str(recursao(n-1)) + str(n)
    
print(recursao(int(input())))