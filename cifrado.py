import sys
from operator import xor

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

input()
