bruto=float(input('Ingrese el Salario Bruto '))
renta=bruto*0.1
social=bruto*0.05
pensiones=bruto*0.03
suma=renta+social+pensiones
neto=bruto-suma
print('El salario neto es de: ', neto)
print('El descuento total es de: ', renta+social+pensiones)
print('El salario bruto es de: ', bruto)
