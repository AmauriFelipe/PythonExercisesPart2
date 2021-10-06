from datetime import date


def votacao(nasc):

    global idade

    idade = date.today().year - nasc

    if idade < 16:
        voto = 'Negado'
    elif 16 <= idade < 18 or idade > 65:
        voto = 'Opcional'
    else:
        voto = 'Obrigatório'

    return voto

nasc = int(input('Digite o ano de nascimento: '))
resultadovoto = votacao(nasc)
print('Com {} anos o voto é {}.'.format(idade, resultadovoto))

