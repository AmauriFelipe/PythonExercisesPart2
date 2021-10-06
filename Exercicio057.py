s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
#while s not in 'MF':
while s != 'F' and s != 'M':
    s = str(input('Resposta inválida. Tente novamente: ')).upper().strip()[0]
print('')
print('Sexo {} registrado com sucesso.'.format(s))