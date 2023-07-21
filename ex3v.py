import numbers


def calcularResultado(url):
    vic = list()
    teste = list()
    
    for kk in range(0, 100):
        teste.append('{}'.format(kk))
    
    for x in url:
        for z in teste:
            if z in x:
                vic.append(z)
    
 
    cc = list()

    for p in vic:
        k = int(p)
        cc.append(k)
    

    final = cc[0] + cc[1]
    pinto = final * cc[2]
    print(pinto)






        

            


calcularResultado('https://www.site.com?base=4&delta=2&altura=3')