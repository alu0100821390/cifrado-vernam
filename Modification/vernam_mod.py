##########################################################################################
## Universidad de La Laguna							 	##
## Escuela Superior de Ingeniería y Tecnología	 				 	##
## Grado en Ingeniería Informática				 		 	##
## Seguridad en Sistemas Informáticos			 			 	##
## Fecha: 14/02/2017							  	 	##
## Autor: Kevin Estévez Expósito (alu0100821390) 				 	##
## 										 	##
## Práctica 1: Cifrado de Vernam (CON MODIFICACIÓN)				 	##
## Descripción: Cifrado y descifrado de mensajes mediante el cifrado de Vernam	 	##
## introduciendo dos claves en ASCII, con las que se realiza un doble cifrado.	 	##
##									 	 	##
## Ejecución: py vernam_mod.py 'mensaje' 'primera_clave_ascii' 'segunda_clave_ascii' 	##
## Ejemplo de ejecución: py vernam_mod.py SOL MAR DIA				 	##
##########################################################################################

import sys
from operator import xor

mensaje = sys.argv[1]	# Se guarda el mensaje pasado por parámetros
mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)	# Se pasa el mensaje a binario y se guarda como string
codigo = sys.argv[2]	# Se guarda la primera clave pasada por parámetros
codigo_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in codigo)	# Se pasa el primer código a binario y se guarda como string
codigo2 = sys.argv[3]	# Se guarda la segunda clave pasada por parámetros
codigo_binario2 = ''.join(bin(ord(x))[2:].zfill(8) for x in codigo2)	# Se pasa el segundo código a binario y se guarda como string
cifrado = ''
descifrado = ''

print ('Mensaje original: ' + mensaje)
print ('Mensaje original en binario: ' + mensaje_binario)
print ('Longitud del mensaje en binario:', len(mensaje_binario))
print ()

print ('Primera clave aleatoria 1: ' + codigo)
print ('Primera clave aleatoria en binario: ' + codigo_binario)
print ('Longitud de la primera clave en binario:', len(codigo_binario))
print ()

print ('Segunda clave aleatoria: ' + codigo2)
print ('Segunda clave aleatoria en binario: ' + codigo_binario2)
print ('Longitud de la segunda clave en binario:', len(codigo_binario2))
print ()

print ('Cifrando...')

for i, c in enumerate(mensaje, start=0):	# Para cada caracter del mensaje...
	aux_xor = xor(xor(ord(mensaje[i]), ord(codigo[i])), ord(codigo2[i]))	# XOR entre los caracteres del mensaje y las dos claves
	cifrado += chr(aux_xor)	# Se concatena el caracter obtenido con la variable 'cifrado'

cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in cifrado)	# Se pasa el cifrado obtenido a binario y se guarda como string

print ('Mensaje cifrado en binario: ' + cifrado_binario)
print ('Mensaje cifrado: ' + cifrado)
print ()

print ('Descifrando...')

for i, c in enumerate(cifrado, start=0):	# Para cada caracter del mensaje cifrado...
	aux_xor = xor(xor(ord(cifrado[i]), ord(codigo[i])), ord(codigo2[i]))	# XOR entre los caracteres del mensaje cifrado y las dos claves
	descifrado += chr(aux_xor)	# Se concatena el caracter obtenido con 'cifrado'

descifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in descifrado)	# Se pasa el cifrado obtenido a binario y se guarda como string

print ('Mensaje original en binario: ' + descifrado_binario)
print ('Mensaje original: ' + descifrado)
