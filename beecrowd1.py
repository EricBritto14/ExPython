def fazTudo(valores):
   lista = list()

   for x in valores:
         lista.append(x)
   lista.sort(reverse=True)
   print(lista[0])




fazTudo([30, 10, 20])