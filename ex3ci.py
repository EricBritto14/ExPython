def calcula_numero_da_senha(senha):
    result_binario = ''
    matriz = list()    
    cont_zero = 0
    cont_um = 0
    
    index = 0
    result_decimal = 0

    for i in senha:
        binario = list(i)
        matriz.append(binario)

    for num in range(0,10):
        for lista in matriz:
            if lista[num] == '1':
                cont_um = cont_um + 1
            else:
                cont_zero = cont_zero + 1
        if cont_um >= cont_zero:
            result_binario = result_binario + '1'
        else:
            result_binario = result_binario + '0'
        cont_um = 0
        cont_zero = 0

    for b in result_binario:
        resto = int(result_binario) % 10
        result_decimal = result_decimal + (resto * (2**index))
        index = index + 1
        result_binario = int(result_binario) // 10
        

    return print(result_decimal)

calcula_numero_da_senha(
    ['0110100000','1001011111','1110001010','0111010101','0011100110','1010011001','1101100100','1011010100','1001100111','1000011000']
)