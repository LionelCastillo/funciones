numero = int(input('ingrese el numero: '))
if (numero % 2 != 0 and numero % 3 != 0) and (numero % 5 != 0 and numero % 7 != 0) and numero % 11 != 0:
    print(numero, 'es un numero primo')
else:
    print(numero, 'no es un numero primo')                    