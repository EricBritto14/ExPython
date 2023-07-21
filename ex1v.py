def calculoDNA(letra1, letra2, dna):
    letraP = 0
    letraM = 0
    for x in dna:
        for y in letra1:
            for b in letra2:
                if y in x:
                    letraP = letraP + 1
                if b in x:
                    letraM = letraM + 1
                
    rF = letraP + letraM
    print(rF)
    return rF 

calculoDNA('A', 'G', 'AACTGGUUGG')