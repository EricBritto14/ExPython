def calcula_top_ocorrencias_de_queries(texto, queries,k):
    semelhantes = list()
    valores = list()
    mapeamento = dict()
    filtrados = list()
    final = list()

    cont = 0
    maior = ()

    text = texto.split(' ')
    
    for i in text:
        for p in queries:
            if p in i:
                semelhantes.append(p)

    for x in queries:
        valor = semelhantes.count(x)
        valores.append(valor)
    
    for num in range(len(valores)):
        mapeamento.update({queries[num] : valores[num]})
        

    for z in range(k):
        for m in mapeamento.items():
            if m[1] > cont:
                maior = m
                cont = m[1]
        cont = 0
        filtrados.append(maior)
        mapeamento.pop(maior[0])
    
    for f in filtrados:
        final.append(f[0])

    return print(final)
    

if __name__ == "__main__":
    calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
    ["a", "em", "i", "el"],2)
