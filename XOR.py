import random

def generar_llave(n):
    return [random.randint(0,1) for _ in range(n)]

def xor_texto(texto, llave):
    datos = texto.encode()  # convierte la palabra a bytes
    return ''.join(chr(datos[i] ^ llave[i]) for i in range(len(datos)))

mensaje = "palabra"
llave = generar_llave(len(mensaje))

encriptado = xor_texto(mensaje, llave)
print("Encriptado:", encriptado)

desencriptado = xor_texto(encriptado, llave)
print("Desencriptado:", desencriptado)