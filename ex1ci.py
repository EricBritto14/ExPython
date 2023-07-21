def ultima_parada(combustivel, comsumo_med, post_gasolina):
    distancia_max = combustivel * comsumo_med
    aux = -1

    for i in post_gasolina:
        if i <= distancia_max and i > aux:
            aux = i
    
    return aux

