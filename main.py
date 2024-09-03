import random

#Creando variable con todas los elementos posibles (72 valores)
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduzca la longitud de la contraseña: "))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(elementos)

print(contraseña)
