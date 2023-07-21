def findClosestBookId():
    estante = [13, 15, 16, 17, 18, 19, 21, 23]
    target = int(input("Qual número do livro deseja colocar? "))
    
    if target < estante[0]:
        print(estante[0])
    if target > estante[0] and target < estante[1]:
        print(estante[0])
    elif target >= estante[1] and target < estante[3]:
        print(estante[2])
    elif target >= estante[2] and target < estante[4]:
        print(estante[3])
    elif target >= estante[3] and target < estante[5]:
        print(estante[4])
    elif target >= estante[4] and target < estante[6]:
        print(estante[5])
    elif target >= estante[5] and target < estante[7]:
        print(estante[6])
    elif target >= estante[7]:
        print(estante[7])


if __name__ == "__main__":
    findClosestBookId()

