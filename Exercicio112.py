from Exercicio111.utilidadescev import dados
from Exercicio111.utilidadescev import moeda


a = dados.leiaDinheiro('Digite o valor: R$')
b = float(input('Aumentar em quanto por cento? '))
c = float(input('Diminuir em quanto por cento? '))

moeda.resumo(a, b, c)
