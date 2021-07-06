# Constanza Cordova
#Karen Cortes
#Gustavo Lizama 

#Iterador 

for i in range(50):
    print("iteración {}".format(i+1))


# cuenta_regresiva

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

i=0

while i < cuenta_regresiva:
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
    i+=1

# solo_pares 

n = int(input("Ingrese un número\n"))

for i in range(0,n+1):
    if i%2 == 0:
        print(i)

# solo_pares_refactor

n = int(input("Ingrese un número\n"))

for i in range(1,n+1):
    if i%2 == 0:
        print(i)

#solo_impares 

n = int(input("Ingrese un número\n"))

for i in range(0,n+1):
    if i%2 != 0:
        print(i)

# suma_pares

n = int(input("Ingrese un número\n"))

suma = 0
for i in range(1,n+1):
    if i%2 == 0:
        suma += i

print(suma)


# genera_patron

n = int(input("ingrese el número de filas\n"))
patron = "" 

for i in range(1,n+1):
    patron +=str(i)
    print(patron)
    
#lorem_generator

archivo = open("lorem.txt")
texto = archivo.read()
n = int(input("Ingrese el numero de parrafos que quiere mostrar \n"))
parrafos = texto.split("\n")

for i in range(n):
    print (parrafos[i]+"\n")

# fuerza_bruta

import string

password = (input("Ingrese contraseña: \n")).lower()


abecedario = string.ascii_lowercase
intento = 0

for i in password:
    for j in abecedario:
        if i == j:
            intento += 1
            break
        else:
            intento += 1

print(str(intento) + " intentos")




