ptv=float(input('Ingrese el tiempo del primer viaje '))
pe=float(input('Ingrese la duracion de la primera escala '))
stv=float(input('Ingrese el tiempo del segundo vuelo '))
se=float(input('Ingrese la duracion de la segunda escala '))
ttc=float(input('Ingrese el tiempo del tercer vuelo '))
primertiempo=ptv+stv
segundotiempo=primertiempo+pe
tercer=segundotiempo+se
total=tercer+ttc
print('El tiempo total de viaje es de: ', total)