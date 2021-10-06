from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 7+1):
    nascimento = int(input('Em que ano a pessoa nasceu: '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('''Ao todo temos {} pessoas maiores de idade e 
{} pessoas menores de idade.'''.format(totmaior, totmenor))