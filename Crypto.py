
def crypto(chave):
    lista_sequencia = [1]
    sequencia, lista_final,numero,lista_sequencia =[],[],[],[] #inicializando as listas que vamos armazernar cada varíavel
    for i in range(len(sequencia)):
        numero.append( i + 2) # adicionando na lista numero ignorando o 1
    contador = 0
    while True:
        soma = 0
        if contador >= len(sequencia):
            break
        else:
            if sequencia[contador] == '+': # Trabalhando com o sinal de +
                lista_sequencia.append(numero[contador])
            elif sequencia[contador] == '-': # Trabalhando com o sinal de -
                resultado = len(sequencia[:contador])
                if not resultado:
                    lista_sequencia.insert(-1,numero[contador])
                else:
                    while True:
                        if sequencia[resultado] != '-' or resultado < 0:
                            break
                        else:
                            soma += 1
                            resultado -= 1
                    lista_sequencia.insert(-soma, numero[resultado])
            resultado += 1
            return lista_sequencia


def crypto(chave):
    lista_sequencia = [1]
    numero =[] #inicializando as listas que vamos armazernar cada varíavel
    for i in range(len(chave)):
        numero.append( i + 2) # adicionando na lista numero ignorando o 1
    contador = 0
    while True:
        soma = 0
        if contador >= len(chave):
            break
        else:
            if chave[contador] == '+': # Trabalhando com o sinal de +
                lista_sequencia.append(numero[contador])
            elif chave[contador] == '-': # Trabalhando com o sinal de -
                resultado = len(chave[:contador])
                if not resultado:
                    lista_sequencia.insert(-1,numero[contador])
                else:
                    while True:
                        if chave[resultado] != '-' or resultado < 0:
                            break
                        else:
                            soma += 1
                            resultado -= 1
                    lista_sequencia.insert(-soma, numero[resultado])
            contador += 1
            return chave


