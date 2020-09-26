#Script : Number race 
'''
    Description:
    randint: generar numeros enteros aleatorios 
    uniform: generar numeros decimales aleatorios
'''
import os
from os import system
from random import randint

'para declarar una funcion se utiliza la plabra def seguida del nombre'
#Fuctions 
def dices () :
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot= d1+d2
    #print("Dice 1: ", d1)
    #print("Dice 2: ", d2)
    return [d1, d2,tot]

#Main :::::::::::::
system("cls")
dato=   int(input("ingrese numero de veces: "))
print("",dato)
i=1
while i<=dato :
    print("Tiro  Nro: ",i)
    dd = dices()
    print("D1: ", dd[0])
    print("D2: ", dd[1])
    print("Total:", dd[2]) 
    i=i+1
    if(dd[0]==6 & dd[1]==6):
        os._exit 
    key= input(":::Lanzar nuevamente:::")

print("******Resultados******")
print("Valor Total de lanzamientos: ", i-1)



