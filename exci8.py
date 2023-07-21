def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    valor_por_km = dict()
    vantagem = dict()

    for km in range(100000):
        valor_emp01 = float(tf1) + (float(vqr1)*km)
        valor_emp02 = float(tf2) + (float(vqr2)*km)
        valor_por_km.update({km : [valor_emp01, valor_emp02]})

    for item in valor_por_km.items():
        quilometragem = item[0]
        valores_emp = item[1]
        if valores_emp[0] > valores_emp[1]:
            vantagem.update({quilometragem : 'Empresa 2'})
        elif valores_emp[0] < valores_emp[1]:
            vantagem.update({quilometragem : 'Empresa 1'})
        elif valores_emp[0] == valores_emp[1]:
            vantagem.update({quilometragem : 'Tanto faz'})
        
    if 'Empresa 1' in vantagem.values() and 'Empresa 2' in vantagem.values() and 'Tanto faz' in vantagem.values():
        for v in vantagem.items():
            if v[1] == 'Tanto faz':
                if anterior == 'Empresa 1':
                    sucessor = 'Empresa 2'
                else:
                    sucessor = 'Empresa 1'
                resultado = f'{anterior} quando a distância < {float(v[0])}, Tanto faz quando a distância = {float(v[0])}, {sucessor} quando a distância > {float(v[0])}'
            anterior = v[1]
    elif 'Empresa 1' in vantagem.values():
        resultado = 'Empresa 1'
    elif 'Empresa 2' in vantagem.values():
        resultado = 'Empresa 2'
    else:
        resultado = 'Tanto faz'

    return resultado
    
    




escolhe_taxi("2.5","1.0","5.0","0.75")