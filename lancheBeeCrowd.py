def lancheL(codigoC, quantidadeC):
    cLanche = list()
    codigoLanche = codigoC
    cLanche.append(codigoLanche)
  
    quantidadeLanche = quantidadeC
    vLanche = list()
    

    vLanche.append([0.00, 4.00, 4.50, 5.00, 2.00, 1.50])
    
    for x in cLanche:
        for y in vLanche:
            valorFinal = y[x] * quantidadeLanche
            print(f'Total: R$ {valorFinal:.2f}')

    return valorFinal

lancheL(5, 20)