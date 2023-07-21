import math

def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    total_horas = 0
    horas = list()
    horas_convertidas = list()
    porcentagens = list()

    for m in minutos_assistidos:
        m = math.ceil(m / 60)
        horas.append(m)

    for index in range(len(horas)):
        if assinante[index] == True:
            horas_convertidas.append(horas[index]*2)
        else:
            horas_convertidas.append(horas[index])

    for hora in horas_convertidas:
        total_horas = total_horas + hora
    
    for x in horas_convertidas:
        porcentagem = round(x * 100 / total_horas)
        porcentagens.append(porcentagem)

    return porcentagens