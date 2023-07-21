def retorna_menor_e_maior_valor_de_vendas(tickets):
    lista = list()
    for i in tickets:
        for x in i:
            lista.append(x)
    
    if lista != []:
        lista.sort()
        while min(lista) < 20:
            del(lista[0])

        while max(lista) > 500:
            del(lista[-1])

        lista = [min(lista), max(lista)]
        return lista
      
    print(lista)
    return lista
   
    
if __name__ == "__main__":
    retorna_menor_e_maior_valor_de_vendas([[200,100],[300]])

