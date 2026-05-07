import random

def generar_llave(n):
    llave = []
    for i in range(n):
        llave.append(random.randint(0,1))
    return llave

def xor_cipher(texto, llave):
    resultado = ""
    i = 0
    while i < len(texto):
        resultado += chr(ord(texto[i]) ^ llave[i])
        i += 1
    return resultado

def mostrar_binario(texto, llave):
    binarios = []
    i = 0
    while i < len(texto):
        binarios.append(format(ord(texto[i]) ^ llave[i], '08b'))
        i += 1
    return binarios

mensaje = "palabra"
llave = generar_llave(len(mensaje))

print("Mensaje original:", mensaje)
print("Llave:", llave)

encriptado = xor_cipher(mensaje, llave)
print("Encriptado:", encriptado)
print("Encriptado en binario:", mostrar_binario(mensaje, llave))

desencriptado = xor_cipher(encriptado, llave)
print("Desencriptado:", desencriptado)