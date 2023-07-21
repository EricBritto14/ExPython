from random import Random, random, randrange
import kkk

print("**********************")
print("Bem vindo ao jogo fiot")
print("**********************")

jogo = int(input("Qual jogo deseja jogar? (1)/(2)"))

if jogo == 1:
    print("Jogo forca")
    kkk.jogar() 
elif jogo == 2:
    print("Teste")