def checa_numero_escondido(numero,numero_oculto):
    str_numero = str(numero)
    str_escondido = str(numero_oculto)

    cont = 0
    tamanho_escondido = len(str_escondido)

    for n in str_numero:
        for e in str_escondido:
            if n == e:
                cont = cont + 1

    if cont == tamanho_escondido:
        return True
    else:
        return False           


checa_numero_escondido(12345, 235)