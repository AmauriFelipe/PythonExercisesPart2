def moeda(p = 0):
    '''
    Mostra o valor como um valor monetário.
    :param p: valor
    :return: R$ a,bc
    '''

    m = 'R$ {:.2f}'.format(p)

    return m


def dobro(p = 0, editmoeda = bool):
    '''
    Calcula o dobro de um valor
    :param p: valor
    :return: dobro do valor
    '''

    d = 2 * p

    if editmoeda == True:
        d = moeda(d)

    return d


def metade(p = 0, editmoeda = bool):
    '''
    Calcula a metade de um valor
    :param p: valor
    :return: metade do valor
    '''

    m = p / 2

    if editmoeda == True:
        m = moeda(m)

    return m


def aumentar(p = 0, porc = 0, editmoeda = bool):
    '''
    Soma um valor a uma dada porcentagem de seu inteiro.
    :param p: valor
    :param porc: porcentagem (em %)
    :return: Resultado final
    '''

    r = p * (1 + porc / 100)

    if editmoeda == True:
        r = moeda(r)

    return r


def diminuir(p = 0, porc = 0, editmoeda = bool):
    '''
    Subtrai uma porcentagem de um valor.
    :param p: valor
    :param porc: porcentagem (em %)
    :return: Resultado final
    '''

    r = p * (1 - porc / 100)

    if editmoeda == True:
        r = moeda(r)

    return r


def resumo(a, b, c):
    '''
    :param a: valor
    :param b: porcentagem pra aumentar
    :param c: porcentagem pra diminuir
    :return: texto indicando os resultados
    '''

    r1 = 2 * a
    r2 = a / 2
    r3 = a * (1 + b / 100)
    r4 = a * (1 - c / 100)

    print('O dobro de {} é {}'.format(moeda(a), moeda(r1)))
    print('A metade de {} é {}'.format(moeda(a), moeda(r2)))
    print('Aumentando {}% a {} temos {}'.format(b, moeda(a), moeda(r3)))
    print('Diminuindo {}% de {} temos {}'.format(c, moeda(a), moeda(r4)))
