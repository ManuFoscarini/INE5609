def inverso(string):
    try:
        lista = list(string)

        print(lista[-1])

        lista.pop(-1)
        string = ''.join(lista)
            
        return inverso(string)

    except:
        return

inverso(input())