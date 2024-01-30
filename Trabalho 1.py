def crypto(chave):
    lista_sequencia = [1]
    numero = []  # inicializando as listas que vamos armazernar cada varíavel
    for i in range(len(chave)):
        numero.append(i + 2)  # adicionando na lista numero ignorando o 1
    contador = 0
    while True:
        soma = 0
        if contador >= len(chave):
            break
        else:
            if chave[contador] == '+':  # Trabalhando com o sinal de +
                lista_sequencia.append(numero[contador])
            elif chave[contador] == '-':  # Trabalhando com o sinal de -
                resultado = len(chave[:contador])
                if not resultado:
                    lista_sequencia.insert(-1, numero[contador])
                else:
                    while True:
                        if chave[resultado] != '-' or resultado < 0:
                            break
                        else:
                            soma += 1
                            resultado -= 1
                    lista_sequencia.insert(-soma, numero[contador])
            contador += 1
    return lista_sequencia


def deYodafy(frase):
    x = frase[1:]
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


def reorganizar(texto):
    for a in range(0, len(texto)):
        a1 = texto[a]
        b = [' ', ',', '[', ']']  # elimina carecteres
        for i in range(0, len(b)):
            a1 = a1.replace(b[i], "")
            texto[a] = a1
    for i in range(0, len(texto), 2):
        x = [int(texto[i]), int(texto[i + 1])]
        inter.insert(i // 2, x)


def merge(intervalos):
    count = 0
    uniao.insert(0, intervalos[0])
    for i in range(0, len(intervalos)):
        for j in range(0, len(uniao)):
            if uniao[j][0] <= intervalos[i][0] <= uniao[j][1]:
                count = 1
                if intervalos[i][1] >= uniao[j][1]:
                    uniao[j] = [uniao[j][0], intervalos[i][1]]
            elif intervalos[i][0] <= uniao[j][0] <= intervalos[i][1]:
                count = 1
                if intervalos[i][1] <= uniao[j][1]:
                    uniao[j] = [intervalos[i][0], uniao[j][1]]
                else:
                    uniao[j] = [intervalos[i][0], intervalos[i][1]]
        if count == 0:
            uniao.append(intervalos[i])
        count = 0


def verificar(conjunto):
    y = 0
    count = 0
    while y == 0:
        y = 0
        for i in range(0, len(conjunto)):
            for j in range(i+1, len(conjunto)):
                if conjunto[j][0] <= conjunto[i][0] <= conjunto[j][1]:
                    count = 1
                    y = 0
                    if conjunto[i][1] >= conjunto[j][1]:
                        conjunto[i] = [conjunto[j][0], conjunto[i][1]]
                elif conjunto[i][0] <= conjunto[j][0] <= conjunto[i][1]:
                    count = 1
                    y = 0
                    if conjunto[i][1] <= conjunto[j][1]:
                        conjunto[i] = [conjunto[i][0], conjunto[j][1]]
                    else:
                        conjunto[i] = [conjunto[i][0], conjunto[i][1]]
                else:
                    y = 1
                if count == 1:
                    del (conjunto[j])
            count = 0
            if len(conjunto) == 1:
                break
        if len(conjunto) == 1:
                y = 1

while True:
    # principal
    processo = 0
    ordens = []
    comando = []
    add = 0
    lista = []

    # merge (globais)
    inter = []
    uniao = []
    processos_ = 0
    cont_ = 0

    while True:
        entrada = list(input().split(' '))  # entrada dos comandos

        if entrada[0] == 'halt':
            break

        elif entrada[0] == 'add':
            add += 1
            quantidade = int(entrada[1])
            for i in range(0, quantidade):  
                cont_ += 1
                ordens.append((cont_, input()))  # listando as ordens
                lista.append(add)
        elif entrada[0]== 'process':
            processos_ += 1


    aux = []
    triplo = []
    for i in ordens:
        aux.append(i)
        if (len(aux) == 3):
            aux.sort(key=lambda x: x[1].split()[0])
            triplo.append(aux)	
            aux = []
    if len(aux) != 0:
        aux.sort()
        triplo.append(aux)
    ordens = []
    for i in triplo:
        for j in range(len(i)):
            ordens.append(i[j][1])

    comando_orfao = len(ordens)

    for i in range(processos_):
        if len(ordens) != 0:
            ordens[i] = list(ordens[i].split(' '))
            del (lista[0])
            comando_orfao -= 1

            if ordens[i][0] == 'crypto':
                codigo = list(ordens[i][1])
                code = crypto(codigo)
                saida = ''
                for item in code:
                    saida += str(item)
                print(saida)

            elif ordens[i][0] == 'deYodafy':
                deYodafy(ordens[i])

            elif ordens[i][0] == 'merge':
                txt = ordens[i][1:]

                reorganizar(txt)
                merge(inter)  # CHAMADA

                if len(uniao) > 1:
                    verificar(uniao)

                print(*uniao, sep=' ')  # SAIDA'

                uniao.clear()
                inter.clear()  # ZERA AS LISTAS

    processos = len(sorted(set(lista)))

    print(f'{processos} processo(s) e {comando_orfao} comando(s) órfão(s).')
