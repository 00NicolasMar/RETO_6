# -*- coding: utf-8 -*-
"""reto6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pMIxxrYqGAm03yvM-KWC8r1dPM12gu_H

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
"""

i = int = 0

while (i < 101):
  i += 1
  potencia = i ** 2
  if i == 101:
    break
  print(i, potencia)

"""Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000."""

numero = 1
while numero <= 999:
    print("números impares: " + str(numero))
    numero += 2

numero = 2
while numero <= 1000:
    print("números pares: " + str(numero))
    numero += 2

"""Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado"""

i = int(input("Ingrese un número natural i mayor o igual que 2: ")) # se realiza el ingreso del dato
if i >= 2: # se verifica que el dato cumpla la condicion de ser mayor o igual a 2
    print(f"Números pares descendentes desde {i} hasta 2:") # esta impresion nos da una claridad a la hora de finalizar todo el programa
    while i >= 2:
        if i % 2 == 0: # aqui se define que siempre y cuando "i" sea mayor o igual a 2 se realice el modulo entre 2 para calcular que el numero sea par
            print(i, end=", ") # aqui se realiza la impresion del resultado separada por comas
        i -= 1
else:
    print("El número ingresado no es válido.") # esta es una impresion realizada en el caso en el cual el numero que ingresemos no cumpla las condiciones

"""Imprimir el factorial de un número natural n dado."""

i = int(input("Ingrese un número natural: ")) # aqui se establece el ingreso del dato
if i >= 0: # se verifica que dicho valor "i" sea mayor o igual a 0
    fact = 1
    cont = 1
    while cont <= i: # aqui se realiza el calculo factorial acumulado a partir de la variable "fact" que significa factorial solo que recorte la palabra un poco
        fact *= cont
        cont += 1

    print(f"El factorial de {i} es: {fact}")
else:
    print("El número no es válido:")

"""Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

"""

def divisores():
    n = input("Ingresa un número entre 2 y 50: ") # aqui se establece el ingreso del dato

    if n.isdigit(): # aqui se verifica si el numero ingresado "n" es positivo (esta es una validacion extra profe asi que pues no esta de mas)
        n = int(n)
        if 2 <= n <= 50: # aqui confirmamos que "n" este en el rango de 2 a 50
            divisor = [i for i in range(1, n + 1) if n % i == 0] # aqui se plantea la operacion para calcular los divisores de el numero n por medio de un modulo
            print(f"Los divisores del numero {n} son: {divisor}") # se imprimen los divisores
        else:
            print("El número no es valido.")
    else:
        print("ingresa un número válido.")
divisores() # termina la funcion

"""Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones"""

def es_primo(n): # se toma a n como argumento con el fin de verificar si es primo
    if n < 2: # aqui se verifica si n es mayor o menor que dos, dandonos falso en el caso de que n sea menor que 2
        return False
    for i in range(2, int(n**0.5) + 1): # aqui se verifica si n es divisible por algun numero en el rango 2 hasta la raiz cuadrada de n, (recuerde si un número n no tiene divisores menores o iguales a raiz de n, es primo). Esto lo establecemos para reducir iteraciones
        if n % i == 0:
            return False
    return True
def primos(rango_in, rango_fin):
    for i in range(rango_in, rango_fin + 1): # se establece el rango de 1 a 101, (recuerde que es 101 ya que es un intervalo semi abierto)
        if es_primo(i): # aqui se abre un condicional "if" si se cumplen las condiciones
            print(i, end=" ") # imprime los primos separados por espacios
primos(1, 100) # es el llamado final a la funcion (algo asi como el cierre de todo el programa)