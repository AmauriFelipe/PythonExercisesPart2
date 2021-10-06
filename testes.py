try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b

except:
    print('Infelizmente faiô... :(')

else:
    print('{} / {} = {}'.format(a, b, c))

finally:
    print('Volte sempre.')
