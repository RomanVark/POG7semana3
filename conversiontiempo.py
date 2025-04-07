total_segundos=int(input('Ingresa la cantidad total de segundos: '))
horas=total_segundos//3600
segundos_usados_para_horas=horas*3600
segundos_restantes=total_segundos-segundos_usados_para_horas
minutos=segundos_restantes//60 
segundos_usados_para_minutos=minutos*60
segundos_finales=segundos_restantes-segundos_usados_para_minutos
print(f'{total_segundos} segundos son {horas} horas, {minutos} minutos y {segundos_finales} segundos.')
