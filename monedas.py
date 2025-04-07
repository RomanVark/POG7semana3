cantidad_dolares=float(input('Ingresa la cantidad en dólares: '))
tasa_euros=float(input('Ingresa la tasa de cambio de dólares a euros: '))
tasa_libras=float(input('Ingresa la tasa de cambio de dólares a libras: '))
tasa_yenes=float(input('Ingresa la tasa de cambio de dólares a yenes: '))
cantidad_euros=cantidad_dolares*tasa_euros
cantidad_libras=cantidad_dolares*tasa_libras
cantidad_yenes=cantidad_dolares*tasa_yenes
print(f'Cantidad en dólares: ${cantidad_dolares:.2f}')
print(f'Equivalente en euros: €{cantidad_euros:.2f}')
print(f'Equivalente en libras: £{cantidad_libras:.2f}')
print(f'Equivalente en yenes: ¥{cantidad_yenes:.2f}')
