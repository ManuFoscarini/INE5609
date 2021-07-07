from circularLinkedList import CircularLinkedList

def solveJosephus(n, m):
    circle = CircularLinkedList()
    z = n
    while z > 0:
        circle.push(z)
        z -= 1
    pivot = circle._tail._next
    while circle._size != 1:
        if m == 1:
            circle._remove(pivot)
            pivot = pivot._next #ok
        else:
            mem = pivot
            j = 1
            while j < m:
                pivot = pivot._next
                j += 1
            if mem._element == pivot._next._element:
                while pivot._next._element == mem._element:
                    pivot = pivot._next
                circle._remove(pivot)
                pivot = pivot._next
            else:
                circle._remove(pivot)
                pivot = pivot._next
    return pivot._element


x = int(input())
i = 0
while i < x:
    n = int(input())
    m = int(input())
    resultado = solveJosephus(n, m)
    i = i + 1
    print("Usando n={}, m={}, resultado={}".format(n, m, resultado))