def ultima_parada(combustivel, comsumo_med, post_gasolina):
    distancia_max = combustivel * comsumo_med
    aux = 0

    for x in post_gasolina:
        if x <= distancia_max and x > aux:
            aux = x
            print(x)
    
    if aux != 0:
        return print(aux)
    else:
        return print(-1)

if __name__ == "__"



    

    


ultima_parada(2, 0, [2, 15, 22, 11])
