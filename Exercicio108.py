import Moeda


r = float(input('Digite o preço: R$ '))
print('O dobro de {} é {}'.format(Moeda.moeda(r), Moeda.moeda(Moeda.dobro(r))))
print('A metade de {} é {}'.format(Moeda.moeda(r), Moeda.moeda(Moeda.metade(r))))
print('Aumentando 10% a {} temos {}'.format(Moeda.moeda(r), Moeda.moeda(Moeda.aumentar(r, 10))))
print('Diminuindo 15% de {} temos {}'.format(Moeda.moeda(r), Moeda.moeda(Moeda.diminuir(r, 15))))
