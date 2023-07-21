def updatePlayersHealth():
  qSoma = int(input("Digite quantos números deseja digitar para a soma: "))
  valorTotal = 0
  s = fazTudo(qSoma, valorTotal)


def fazTudo(qSoma, valorTotal):
    for x in range(qSoma):
        numeros = input("Digite o número escrito que deseja somar: ")
        numeros = numeros.strip().lower()
        if numeros == "um":
            numeros = 1
            valorTotal = valorTotal + numeros
        elif numeros == "dois":
            numeros = 2
            valorTotal = valorTotal + numeros
        elif numeros == "tres":
            numeros = 3
            valorTotal = valorTotal + numeros
        elif numeros == "quatro":
            numeros = 4
            valorTotal = valorTotal + numeros
        elif numeros == "cinco":
            numeros = 5
            valorTotal = valorTotal + numeros
        elif numeros == "seis":
            numeros = 6
            valorTotal = valorTotal + numeros
        elif numeros == "sete":
            numeros = 7
            valorTotal = valorTotal + numeros
        elif numeros == "oito":
            numeros = 8
            valorTotal = valorTotal + numeros
        elif numeros == "nove":
            numeros = 9
            valorTotal = valorTotal + numeros
        elif numeros == "dez":
            numeros = 10
            valorTotal = valorTotal + numeros
        else:
            valorTotal = valorTotal - 1

    return print("O valor total é {}".format(valorTotal))

    

if __name__ == "__main__":
    updatePlayersHealth()

