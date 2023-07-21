def intervalo(valorInserido, intervalos):
    lista = list()

    for x in intervalos:
        lista.append(x)
    
    lista.sort()
    print(lista)
    
    for p in lista:
        for x in valorInserido:
            if x <= p:
                print(p)
    



intervalo([(24.50)], [(0.25), (25.50), (50.75), (75.100)])