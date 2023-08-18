'''
script en python que convierte los segundos a minutos, 
horas y los minutos a segundos y horas
y tambien tiene un menu de opciones 
'''
import os 

# las variables  constantes del tiempo
SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60

# variables para el menu
SEGUNDOS_A_MINUTOS = 1
SEGUNDOS_A_HORAS = 2
MINUTOS_A_SEGUNDOS = 3
MINUTOS_A_HORAS = 4
SALIR = 0


# funciones para la conversion de valores del tiempo
def segundos_a_minutos(segundos):
	mins = segundos // SEGUNDOS_POR_MINUTO
	segs = segundos % SEGUNDOS_POR_MINUTO

	return mins, segs

def minutos_a_segundos(minutos, segundos):
	segs = minutos * SEGUNDOS_POR_MINUTO + segundos

	return segs

def minutos_a_horas(minutos, segundos):
	hrs = minutos // MINUTOS_POR_HORA
	mins = minutos % MINUTOS_POR_HORA
	segs = segundos

	return hrs, mins, segs

def segundos_a_horas(segundos):
	mins, segs = segundos_a_minutos(segundos)
	hrs, mins, segs = minutos_a_horas(mins, segs)

	return hrs, mins, segs

# el menu para seleccionar los valores que queremos convertir
def menu():
	print(f'''       converciones

	{SEGUNDOS_A_MINUTOS}) segundos a minutos
	{SEGUNDOS_A_HORAS}) segundos a horas
	{MINUTOS_A_SEGUNDOS}) minutos a segundos
	{MINUTOS_A_HORAS}) minutos a horas
	{SALIR}) salir

		''')

# funcion para la logica y el funcionamiento del script
def main():
	continuar = True
	while continuar: 
		os.system('cls')
		menu()
		opc = int(input('selecciona una opcion: '))
		os.system('cls')
		if opc == SEGUNDOS_A_MINUTOS:
			s = -1
			while 0 > s:
				s = int(input('cantidad de segundos a convertir: '))
			mins, segs = segundos_a_minutos(s)
			print(f'el equivalente es {mins}:{segs}')
		elif opc == SEGUNDOS_A_HORAS:
			s = -1
			while 0 > s:
				s = int(input('cantidad de  segundos a convertir: '))
			hrs, mins, segs = segundos_a_horas(s)
			print(f'el equivalente es {hrs}:{mins}:{segs}')
		elif opc == MINUTOS_A_SEGUNDOS:
			m = -1
			while 0 > m:
				m = int(input('cantidad de minutos a convertir: '))
			s = -1
			while 0 > s or s >= SEGUNDOS_POR_MINUTO:
				s = int(input('cantidad de segundos a convertir: '))
			segs = minutos_a_segundos(m, s)
			print(f'el equivalente es {segs}')
		elif opc == MINUTOS_A_HORAS:
			m = -1 
			while 0 > m:
				m = int(input('cantidad de minutos a convertir: '))
			s = -1
			while 0 > s or s >= SEGUNDOS_POR_MINUTO:
				s = int(input('cantidad de segundos a convertir: '))
			hrs, mins, segs = minutos_a_horas(m, s)
			print(f'el equivalente es {hrs}:{mins}:{segs}')
		elif opc == SALIR:
			print('nos vemos cara de monda')
			continuar = False
		else:
			print('opcion no validad')
		input('preciona enter para continuar')


# if __name__ == '__main__' esta condicional sirve para cuando el modulo es importado solo se ejecute 
# si es nombrado donde se esta solicitando la importacion del modulo
if __name__ == '__main__':
	main()

