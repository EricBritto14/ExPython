def shuffle_musicas(musicas_tocadas):
    listaF = list()
    listaP = list()
    for x in musicas_tocadas:
        p = max(musicas_tocadas)
        listaF.append(p)
        del(musicas_tocadas[1])

    for y in musicas_tocadas:
        listaP.append(y)

    res = listaF + listaP
    res[::2] = listaF
    res[1::2] = listaP
    return str(res)

shuffle_musicas([2,10,5,3]) 