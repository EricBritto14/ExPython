def multiplos(A, B):
    valor1 = list()
    valor1.append(A)

    valor2 = list()
    valor2.append(B)

    for x in valor1:
        for y in valor2:
            f = y%x
        
    if f != 0:
        print("Não são Multiplos")
    else:
        print("São Multiplos")

multiplos(6, 25)