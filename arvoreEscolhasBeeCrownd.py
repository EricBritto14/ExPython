def escolhas(escolha):
    v = escolha
    resultado = list()
    resultado.append(v)
    verdadeiro = list()

    final = list()
    p = ['vertebrado, mamifero']
    final.append(p)
    
    for x in resultado:
        print(x)
        for y in final:
                print(y)
                for x in y:
                    print(x)
                    
                    verdadeiro.append(y)
               
    
escolhas(['vertebrado, mamifero, onivoro'])