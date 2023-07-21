def calculoSoma():
    n1 = int(input("Digite o primeiro número para fazer a soma: "))
    n2 = int(input("Digite o segundo número para fazer a soma: "))
    print("SOMA = ", somaSimples(n1, n2))

def multi():
    nm = int(input("Digite o primeiro número para o produto: "))
    nm2 = int(input("Digite o primeiro número para o produto: "))
    print("PROD = ", multiplicar(nm, nm2))


def calculoRaio():
    n = 3.14159
    r = int(input("Digite o valor do ráio para o calculo: "))
    print("A: ", raio(n, r))

def multiplicar(nm, nm2):
    return nm*nm2

def raio(n, r):
    return n*(r*r)

def somaSimples(n1, n2):
    return n1 + n2 


if __name__ == "__main__":
    multi()
