def calcular_total_leds(altura, largura):
    if altura == 0 or largura == 0:
        return 0

    resultado = (altura + 1) * (largura + 1)

    return resultado