from random import random
import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    palavras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(palavras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pedir_chute()
        # Strip para tirar os espaços da letra, se o cara jogasse espaço só dava ruim

        if (chute in palavra_secreta):
            chute_correto(palavra_secreta, chute,  palavras_acertadas)
        else:
            erros += 1
            desenho_forca(erros)
            

        enforcou = erros == 7
        acertou = "_" not in palavras_acertadas
        print(palavras_acertadas)

    if acertou:
        imprime_mensagem_venceu()
    else:
        imprime_mensagem_pinou(palavra_secreta)


def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_abertura():
    print("**********************")
    print("Bem vindo ao jogo da forca")
    print("**********************")


def carrega_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pedir_chute():
    chute = input("Digite uma letra para jogar: ")
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra_secreta, chute, palavras_acertadas):
    index = 0
    for letra in palavra_secreta:
           if (chute == letra):
                palavras_acertadas[index] = letra
           index += 1

def imprime_mensagem_venceu():
    print("Parabéns, você cagou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_pinou(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
   


if __name__ == "__main__":
    jogar()

# Acessando a lista, e colocando no espaço dela o valor do chute.
    # Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função .count()
    # função len para saber o tamanho da lista ou tuple, min valor minimo, max valor maximo, append para inserir coisas a lista
    # a função .index(), que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista
    # list[] é mutável, tuple() é imutável
    # Para adicionar um elemento a um set invez de lista, devemos chamar a função add (ao invés da append que é pra lista):

    # Criando um Dictionary
    # instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
    # São sempre com chaves {} e em pares, por exemplo o Nico com idade 39, assim fica mais facil de procurar algum valor dentro desse dictionary
    # Só criar um instrutores['Flavio'] e já acharia ele dentro desse dictionary com sua idade 37
