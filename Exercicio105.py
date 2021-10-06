def notas(* n , situacao = bool):

    '''
    Função para analisar notas
    :param n: Valores float
    :param situacao: Valor bool
    :return: dicionário com informações sobre as notas
    '''

    dicionotas = {}

    media = sum(n) / len(n)

    dicionotas['total de notas'] = (len(n))
    dicionotas['maior nota'] = max(n)
    dicionotas['menor nota'] = min(n)
    dicionotas['media'] = media

    if situacao == True:
        if media < 6:
            dicionotas['Situação'] = 'Ruim'
        elif 6 <= media:
            dicionotas['Situação'] = 'Aceitável'

    return dicionotas


# Programa principal

resp = notas(7, 3, 9, 5, 10, 3, 8, situacao = True)
print(resp)

help(notas)
