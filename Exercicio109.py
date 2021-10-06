import Moeda


r = float(input('Digite o preço: R$ '))
print('O dobro de {} é {}'.format(Moeda.moeda(r), Moeda.dobro(r, editmoeda = True)))
print('A metade de {} é {}'.format(Moeda.moeda(r), Moeda.metade(r, editmoeda = True)))
print('Aumentando 10% a {} temos {}'.format(Moeda.moeda(r), Moeda.aumentar(r, 10, editmoeda = True)))
print('Diminuindo 15% de {} temos {}'.format(Moeda.moeda(r), Moeda.diminuir(r, 15, editmoeda = True)))
