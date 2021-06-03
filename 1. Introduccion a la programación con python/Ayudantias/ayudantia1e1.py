#Ejercicio 1

#Supongamos que has abierto una nueva cuenta de ahorro que te da una ganancia de 4
#% de interés anual. Los intereses ganados se pagan al final de cada año y se agregan al
#balance de la cuenta de ahorro. Escribe un programa que lea la cantidad de dinero
#depositada en la cuenta inicialmente. El programa debe calcular y mostrar el balance de
#la cuenta de ahorros luego de 1, 2 y 3 años. Mostrar cada cantidad redondeada al
#segundo decimal. tip: buscar la función round().
import sys
saldo = int(sys.argv[1])
n =3
balance = 0
for i in range(1,n+1):
    balance = round(1.04*saldo, 2)
    print(f"año {i}: saldo inicial {saldo}, saldo final: { balance}")
    saldo = balance
