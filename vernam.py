###################################################################################
## Universidad de La Laguna						 								 ##
## Escuela Superior de Ingeniería y Tecnología	 								 ##
## Grado en Ingeniería Informática				 								 ##
## Seguridad en Sistemas Informáticos			 								 ##
## Fecha: 14/02/2016							 								 ##
## Autor: Kevin Estévez Expósito (alu0100821390) 								 ##
## 																				 ##
## Práctica 1: Cifrado de Vernam												 ##
## Descripción: Cifrado y descifrado de mensajes mediante el cifrado de Vernam	 ##
##											 								 	 ##
## Ejecución: py vernam.py 'mensaje' 'clave_binaria'							 ##
## Ejemplo de ejecución: py vernam.py SOL 001111000001100001110011			 	 ##
###################################################################################


import sys
from operator import xor

opcion =''

opcion = str(input('¿Quiere [c]ifrar o [d]escifrar el mensaje?: '))
while opcion != 'c' and opcion != 'd':	# Mientras la opción introducida no sea correcta...
	print ()
	print ('Opción no válida!')
	opcion = str(input('¿Quiere [c]ifrar o [d]escifrar el mensaje?: '))
print ()

if opcion == 'c':	# Si se desea cifrar un mensaje...
	mensaje = sys.argv[1]	# Se guarda el mensaje pasado por parámetros
	mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)	# Se pasa el mensaje a binario y se guarda como string
	codigo = sys.argv[2]	# Se guarda la clave pasada por parámetros
	cifrado = ''

	print ('Mensaje original: ' + mensaje)
	print ('Mensaje original en binario: ' + mensaje_binario)
	print ('Longitud del mensaje binario:', len(mensaje_binario))
	print ('Clave aleatoria: ' + codigo)

	for i, c in enumerate(mensaje, start=0):	# Para cada caracter del mensaje...
		aux_xor = xor(ord(c), ord(chr(int(codigo[i*8:(i+1)*8], base=2))))	# XOR entre el caracter y el byte correspondiente de la clave
		cifrado += chr(aux_xor)	# Se concatena el caracter obtenido con 'cifrado'

	cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)	# Se pasa el cifrado obtenido a binario y se guarda como string

	print ('Mensaje cifrado en binario: ' + cifrado_binario)
	print ('Mensaje cifrado: ' + cifrado)
	
elif opcion == 'd':	# Si se desea descifrar un mensaje...
	cifrado = sys.argv[1]	# Se guarda el cifrado pasado por parámetros
	cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in cifrado)	# Se pasa el cifrado a binario y se guarda como string
	codigo = sys.argv[2]	# Se guarda la clave pasada por parámetros
	mensaje = ''

	print ('Mensaje cifrado: ' + cifrado)
	print ('Mensaje cifrado en binario: ' + cifrado_binario)
	print ('Longitud del mensaje binario:', len(cifrado_binario))
	print ('Clave aleatoria: ' + codigo)

	for i, c in enumerate(cifrado, start=0):	# Para cada caracter del cifrado...
		aux_xor = xor(ord(c), ord(chr(int(codigo[i*8:(i+1)*8], base=2))))	# XOR entre el caracter y el byte correspondiente de la clave
		mensaje += chr(aux_xor)	# Se concatena el caracter obtenido con 'mensaje'

	mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)	# Se pasa el mensaje obtenido a binario y se guarda como string

	print ('Mensaje original en binario: ' + mensaje_binario)
	print ('Mensaje original: ' + mensaje)

else:
	print ('Ha ocurrido un error inesperado. Terminando ejecución.')
	sys.exit(1)
