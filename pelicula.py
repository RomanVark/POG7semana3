duracion_pelicula=int(input('Ingresa la duración de la película en minutos: '))
comerciales_previos=int(input('Ingresa la duración de los comerciales previos (en minutos): '))
cantidad_pausas=int(input('Ingresa la cantidad de pausas comerciales durante la película: '))
duracion_pausa=int(input('Ingresa la duración de cada pausa comercial (en minutos): '))
comerciales_durante=cantidad_pausas*duracion_pausa
duracion_total=duracion_pelicula+comerciales_previos+comerciales_durante
print(f'Duración original de la película: {duracion_pelicula} minutos')
print(f'Duración de comerciales previos: {comerciales_previos} minutos')
print(f'Duración total de comerciales durante la película: {comerciales_durante} minutos')
print(f'Tiempo total de la proyección: {duracion_total} minutos')
