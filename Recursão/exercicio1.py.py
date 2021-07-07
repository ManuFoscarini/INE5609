def counter(string):
    try:
        lista = list(string)
        
        lista.pop(0)

        return 1 + counter(string[1:])

    except:
        return 0

print(counter(input()))