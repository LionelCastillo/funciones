from math import pi

base = float(input('ingrese la base del triangulo en cms: '))
altura = float(input('ingrese la altura del triangulo en cms: '))
area_triangulo = float((base*altura)/2)
print('el area del triangulo es ', area_triangulo, 'cms**2')
radio = float(input('ingrese el radio del circulo en cms'))
area_circulo = float(pi*(radio**2))
print('el area del circulo es', area_circulo, 'cms**2')    