import Moeda


r = float(input('Digite o preço: R$ '))
print('O dobro de R${} é R${}'.format(r, Moeda.dobro(r)))
print('A metade de R${} é R${}'.format(r, Moeda.metade(r)))
print('Aumentando 10% a R${} temos R${}'.format(r, Moeda.aumentar(r, 10)))
print('Diminuindo 15% de R${} temos R${}'.format(r, Moeda.diminuir(r, 15)))
