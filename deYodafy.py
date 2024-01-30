def deYodafy(comando):
    x = comando[1:]
    a = x[len(x) - 1]
    b = a[:len(a) - 1]
    c = a[-1]
    lista = []
    for i in range(0, 2 * len(x)):
        if i % 2 == 0:
            lista.insert(i, x[len(x) - i // 2 - 1])
        else:
            lista.insert(i, ' ')

    lista[0] = b
    lista[len(lista) - 1] = c
    print("".join(lista))

