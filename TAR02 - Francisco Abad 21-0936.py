#Escribir un programa que pida 2 numeros y muestre paso a paso el calculo de la raiz cuadrada de la raiz cuadrada de la suma del cuadrado de ambos
#Francisco Abad 21-0936

from cmath import sqrt #Importamos la libreria math.
import math

num1=int(input('Escriba el primer numero:')) #Declaramos las variables para la entrada al teclado.
num2=int(input('Escriba el segumdo numero:'))

potencia1=pow(num1,2) #Elevamos al cuadrado cada variable y luego imprimimos esa potencia.
potencia2=pow(num2,2)
print(potencia1)
print(potencia2)

suma=(potencia1+potencia2) #Se suman la potencias de las variables.
print(suma) 

raiz=sqrt(suma) #Se hace la radicacion de las potencias.
print(raiz)