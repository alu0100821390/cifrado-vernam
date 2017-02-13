import sys
from operator import xor

opcion =''

opcion = str(input('¿Quiere [c]ifrar o [d]escifrar el mensaje?: '))
while opcion != 'c' and opcion != 'd':
	print ()
	print ('Opción no válida!')
	opcion = str(input('¿Quiere [c]ifrar o [d]escifrar el mensaje?: '))
print ()

if opcion == 'c':
	mensaje = sys.argv[1]
	mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)
	codigo = sys.argv[2]
	cifrado = ''

	print ('Mensaje original: ' + mensaje)
	print ('Mensaje original en binario: ' + mensaje_binario)
	print ('Longitud del mensaje binario:', len(mensaje_binario))
	print ('Clave aleatoria: ' + codigo)

	aux = ''
	for i, c in enumerate(mensaje, start=0):
		xor = ord(c) ^ ord(chr(int(codigo[i*8:(i+1)*8], base=2)))
		cifrado += chr(xor)

	cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)

	print ('Mensaje cifrado en binario: ' + cifrado_binario)
	print ('Mensaje cifrado: ' + cifrado)
	
elif opcion == 'd':
	cifrado = sys.argv[1]
	cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in cifrado)
	codigo = sys.argv[2]
	mensaje = ''

	print ('Mensaje cifrado: ' + cifrado)
	print ('Mensaje cifrado en binario: ' + cifrado_binario)
	print ('Longitud del mensaje binario:', len(cifrado_binario))
	print ('Clave aleatoria: ' + codigo)

	for i, c in enumerate(cifrado, start=0):
		xor = ord(c) ^ ord(chr(int(codigo[i*8:(i+1)*8], base=2)))
		mensaje += chr(xor)

	mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje)

	print ('Mensaje original en binario: ' + mensaje_binario)
	print ('Mensaje original: ' + mensaje)

else:
	print ('Ha ocurrido un error inesperado. Terminando ejecución.')
	sys.exit(1)
