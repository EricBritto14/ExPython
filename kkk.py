from random import Random, random, randrange
from unicodedata import name


def jogar():

 print("**********************")
 print("Bem vindo ao jogo fiot")
 print("**********************")

   # Randrange método para gerar números randoms entre 1, 100
 valorFinal = randrange(1, 101)
 totalTentativas = 0
 pontosJogo = 1000

 print(valorFinal)

 print("Qual o nível de díficuldade do jogo você deseja?")
 nivelJogo = int(input("(1)Facil, (2)Médio, (3)Díficil, (4)Want a god of war"))

 if nivelJogo == 1:
    totalTentativas = 20
 elif nivelJogo == 2:
    totalTentativas = 10
 elif nivelJogo == 3:
    totalTentativas = 5
 elif nivelJogo == 4:
    totalTentativas = 2

 rodada = 1
 while (totalTentativas >= rodada):
    print("\nVocê está na {} rodada de {}, tente sua resposta!".format(
        rodada, totalTentativas))
    v = int(input("Digite um número e tente adivinhar o número selecionado: "))

    acertouValor = valorFinal == v
    valorMenor = valorFinal > v
    valorMaior = valorFinal < v

    if acertouValor:
        print("Acertou o valor cagando e fez {} pontos!".format(pontosJogo))
        break
    else:
        print("Errou o valor, pinou!")
        if valorMenor:
            print("O seu número é menor do que o do jogo")
        elif valorMaior:
            print("O seu valor inserido é maior que o valor do jogo")
        # o objetivo dessa função é retornar o número desconsiderando o seu sinal por exemplo se o número for 21 e o chute 30... 21-30 ficaria -10
        pontosPerdidos = abs(valorFinal - v)
        pontosJogo = pontosJogo - pontosPerdidos
    rodada = rodada + 1
 print("O valor final era {}".format(valorFinal))
   
if __name__ == "__main__":
    jogar()
#Esse __name__ e __main__ verificam se estão na main do projeto, se ele está sendo puxado em outro programa
#Como por exemplo no teste.py, ele não vai executar diretamente pq lá não é main


#"R$ {:7.1f}".format(1000.12)
#"R$ {:07.2f}".format(4.11)

