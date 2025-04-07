pi=3.1416
radio=float(input('Ingresa el radio del cilindro: '))
altura=float(input('Ingresa la altura del cilindro: '))
area_base=pi*radio**2
volumen=area_base*altura
area_lateral=2*pi*radio*altura
area_total=area_lateral+2*area_base
print(f'Radio ingresado: {radio}')
print(f'Altura ingresada: {altura}')
print(f'Volumen calculado: {volumen:.2f}')
print(f'Área superficial calculada: {area_total:.2f}')