print("**********************")
print("Bem vindo ao jogo fiot")
print("**********************")

print("\n**********************")

print("**********************")


valorFinal = 42

totalTentativas = 5


for rodada in range(1, totalTentativas):
        print("\nVocê está na {} rodada de {}, tente sua resposta!".format(rodada, totalTentativas + 1))
        v = int(input("Digite um número entre 1-100 e adivinhe o número selecionado: "))
        acertouValor = valorFinal == v
        valorMenor = valorFinal > v
        valorMaior = valorFinal < v

        if v < 0 or v > 100:
            print("O fi, é maior que 0 e menor que 100 não entendeu não?")
            continue

        elif acertouValor:
            print("Acertou o valor cagando e acabou com o jogo!")
            break

        else:
            print("Errou o valor, pinou!")
            if valorMenor:
                print("O seu número é menor do que o do jogo")
            elif valorMaior:
                print("O seu valor inserido é maior que o valor do jogo")

#"R$ {:7.1f}".format(1000.12)
#"R$ {:07.2f}".format(4.11)

r = 3 / 2
print(r) 

# // sempre devolve um valor inteiro, 3//2 volta 1.0