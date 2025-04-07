peso=float(input('Ingresa el peso en KG: '))
altura=float(input('Ingresa la altura en metros '))
altura_cuadrado=altura*altura
imc=peso/altura_cuadrado
imc_redondeado=round(imc*100)/100
print(f'Peso en kg: , {peso} kg')
print(f'Altura en M: , {altura} M')
print(f'Icm calculado es de: , {imc_redondeado}')
if imc_redondeado<18.5:
    clasificacion='Bajo peso'
elif 18.5<=imc_redondeado<25:
    clasificacion='Peso norma'
elif 25<=imc_redondeado<30:
    clasificacion='Sobrepeso'
else:
    clasificacion='Obesidad'
print(f'Clasificación: {clasificacion}')
