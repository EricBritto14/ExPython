def fazTudo():
    s = int(input("Digite quantos números deseja multiplicar: \n"))
    final = 1
    
    for x in range(s):
        p = int(input("Digite os números: \n"))
        final = final * p 
        p = 0

    
    print(final)


if __name__ == "__main__":
    fazTudo()