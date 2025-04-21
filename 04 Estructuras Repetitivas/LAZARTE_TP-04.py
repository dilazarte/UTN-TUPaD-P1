import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos)

for i in range(1, 100+1):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

# numero = int(input("Ingrese un numero positivo: "))
# contador=0
# if numero < 0:
#     print("Te dije numero positivo!!!")
#     exit()
# for i in range (len(str(numero))):
#     contador+=1
# print(F"la cantidad de digitos que tiene el numero es: {contador}")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# n1 = int(input("Ingrese un numero positivo: "))
# n2 = int(input("Ingrese otro numero positivo: "))
# suma=0

# for i in range(n1+1, n2):
#     suma+=i
# print(suma)


# 4)  Elabora un programa que permita al usuario ingresar números enteros y los sume en  secuencia.
    #El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

# n = int(input("Ingrese un numero: "))
# suma=0

# while(n != 0):
#     suma+=n
#     n = int(input("Ingrese otro numero: "))

# print(F"lla suma total es: {suma}")


# 5)  Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# n = int(input("Adivine el numero del 0 al 9, ingrese un numero: "))
# intentos=1
# nr = random.randint(0,9)

# while(n != nr):
#     intentos+=1
#     n = int(input("fallaste! ingresa un numero de nuevo: "))

# print(F"bien!!, adivinaste, el numero secreto es {nr} y realizaste {intentos} intentos!!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente

# for i in range(100-2,0,-2):
#     print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

# n = int(input("ingrese un numero positivo: "))
# suma=0
# if n < 0:
#     print("Te dije numero positivo!!!")
#     exit()

# for i in range (n+1):
#     suma+=i

# print(F"la suma del 0 hasta el {n} es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares
# cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# CANTIDAD=5 ##cambiar aca segun la cantidad de numeros que se desee
# contador=0
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# while(contador < CANTIDAD):
#     n = int(input(f"ingrese el numero nº {contador+1}: "))
    
#     if n % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
    
#     if n > 0:
#         positivos += 1
#     elif n < 0:
#         negativos += 1
    
#     contador+=1

# print(F"positivos: {positivos}")
# print(F"negativos: {negativos}")
# print(F"pares: {pares}")
# print(F"impares: {impares}")


# 9)  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

# CANTIDAD=5
# contador=0
# suma=0

# print(f"calculando la media de {CANTIDAD} numeros")

# while(contador < CANTIDAD):
#     n = int(input(f"ingrese el numero nº {contador+1}: "))
#     suma+=n
#     contador+=1

# print(f"La media para {CANTIDAD} numeros ingresados es: {suma/CANTIDAD}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# n = int(input("ingrese un numero positivo para ver su inverso: "))
# inverso = str(n)[::-1]

# print(f"el inverso de {n} es: {inverso}")