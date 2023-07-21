def fazTudo():
    X1 = int(input('Horas do 1 trem: \n'))
    Y1 = int(input('Minutos do 1 trem: \n'))
    W1 = int(input('Km percorrido pelo trem: \n'))
    Z1 = int(input('Velocidade média percorrida pelo trem: \n'))

    tempoFinalTrem = W1 / Z1
    tempoFinalTrem 
    horasFinal = X1 + tempoFinalTrem
    p = int (horasFinal)
    
    X2 = int(input('Horas do 2 trem: \n'))
    Y2 = int(input('Minutos do 2 trem: \n'))
    W2 = int(input('Km percorrido pelo trem: \n'))
    Z2 = int(input('Velocidade média percorrida pelo trem: \n'))

    tempoFinalTrem2 = W2 / Z2
    horasFinal2 = X2 + tempoFinalTrem2
    p2 = int (horasFinal2)
    #pf = p + p2  Confundi


    if p2 > 23:
        print('False')
    if p2 < 0:
        print('False')
    if p2 <= 23:
        print('Verdadeiro')

if __name__ == "__main__":
    fazTudo()

