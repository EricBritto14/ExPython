def calculaEstoqueFinal(estoqueInicial, transacaoes):
    ovo = estoqueInicial
    
    lista = list()
    for x in transacaoes:
        
        lista.append(x)
    
    s = sum(lista)
    final = s + ovo
    print(final)
    return final

    


calculaEstoqueFinal(10, [(-4), (-2), (5), (-1)])