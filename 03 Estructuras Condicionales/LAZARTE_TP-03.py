from statistics import mode, median, mean
import random

#1)
edad = int(input("ingrese su edad:"));
if edad > 18:
    print("Es mayor de edad");


#2)
# nota = int(input("ingrese su nota:"));
# if nota >= 6:
#     print("Aprobado");
# else:
#     print("Desaprobado");


#3)
# numero = int(input("ingrese numero par:"));
# if (numero % 2 == 0):
#     print("Ha ingresado un número par");
# else:
#     print("Por favor, ingrese un número par");


#4)
# edad = int(input("ingrese su edad:"))
# if edad < 12:
#     print("Niño/a")
# elif edad < 18:
#     print("Adolescente")
# elif edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")


#5)
# clave = input("ingrese su contraseña:");
# if (len(clave) >= 8 and len(clave) <= 14):
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6)
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# moda=mode(numeros_aleatorios)
# mediana=median(numeros_aleatorios)
# media=mean(numeros_aleatorios)
# # # print(moda)
# # # print(mediana)
# # # print(media)
# if moda < mediana < media:
#     print("sesgo positivo")
# elif media < mediana < moda:
#     print("sesgo negativo")
# elif moda == mediana == media:
#     print("no hay sesgo")
# else:
#     pass


#7)
# palabra = input("ingrese una palabra o frase:");
# if(palabra[-1] in "aeiou" or palabra[-1] in "AEIOU"):
#     palabra = palabra + "!"
# print(palabra)


#8)
# nombre = input("ingrese su nombre por favor:");
# print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO");
# print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro");
# print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro");
# opcion = input("ingrese una opcion favor:");
# if opcion == "1": print(nombre.upper())
# elif opcion == "2": print(nombre.lower())
# elif opcion == "3": print(nombre.title())
# else: print("La opcion no existe!")


#9)
# magnitud = float(input("ingrese la magnitud del terremoto:"))
# if magnitud < 3:
#     print("Muy leve (imperceptible).")
# elif magnitud < 4:
#     print("Leve (ligeramente perceptible).")
# elif magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños).")
# elif magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras débiles).")
# elif magnitud < 7:
#     print("Muy Fuerte (puede causar daños significativos).")
# else:
#     print("Extremo (puede causar graves daños a gran escala).")


#10)
# hemisferio = input("ingrese el hemisferio en donde se encuentra (N/S):").upper()
# mes = int(input("ingrese el mes (del 1 al 12):"))
# dia = int(input("ingrese el día:"))
# if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#     estacion_norte = "Invierno"
#     estacion_sur = "Verano"
# elif (mes == 3 and dia >= 21) or(mes in [4, 5]) or (mes == 6 and dia <= 20):
#     estacion_norte = "Primavera"
#     estacion_sur = "Otoño"
# elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#     estacion_norte = "Verano"
#     estacion_sur = "Invierno"
# elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
#     estacion_norte = "Otoño"
#     estacion_sur = "Primavera"
# else:
#     estacion_norte = estacion_sur = "Fecha no valida"

# if hemisferio == "N":
#     print(f"Hemisferio norte - Estación: {estacion_norte}")
# elif hemisferio == "S":
#     print(f"Hemisferio sur - Estación: {estacion_sur}")
# else:
#     print("Hemisferio no válido. Usá 'N' para norte o 'S' para sur.")
