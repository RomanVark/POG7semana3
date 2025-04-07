precio_original=float(input('Ingresa el precio original del producto: '))
porcentaje_descuento=float(input('Ingresa el porcentaje de descuento (%): '))
descuento=(precio_original*porcentaje_descuento)/100
precio_con_descuento=precio_original-descuento
porcentaje_iva=float(input('Ingresa el porcentaje de IVA (%): '))
iva_calculado=(precio_con_descuento*porcentaje_iva)/100
precio_final=precio_con_descuento+iva_calculado
print(f'Precio original: ${precio_original:.2f}')
print(f'Descuento aplicado: ${descuento:.2f}')
print(f'Precio con descuento: ${precio_con_descuento:.2f}')
print(f'IVA calculado: ${iva_calculado:.2f}')
print(f'Precio final: ${precio_final:.2f}')