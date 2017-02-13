import sys
from operator import xor

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

input()
