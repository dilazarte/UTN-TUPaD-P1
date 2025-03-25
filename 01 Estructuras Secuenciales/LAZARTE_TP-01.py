#COMENTAR / DESCOMENTAR PARA PROBAR (ctrl + k + u para descomentar, ctrl + k + c para comentar)

# 1) --------[[Hola mundo]]-----------
# print("Hola Mundo!")


# 2) --------[[Pedir nombre y saludar]]-----------
# nombre = input("Por favor, ingrese su nombre: ")
# print(f"Hola {nombre}!")


# 3) --------[[Pedir nombre, apellido, edad, pais y mostrar mensaje]]-----------
# nombre = input("Por favor, ingrese su nombre: ")
# apellido = input("Por favor, ingrese su apellido: ")
# edad = int(input("Por favor, ingrese su edad: "))
# pais = input("Por favor, ingrese su pais: ")
# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}!")


# 4) --------[[Pedir radio y devolver area y perimetro]]-----------
# radio = float(input("Por favor, ingrese el radio de un circulo: "))
# area = 3.141592653589793*radio*radio
# perimetro = 2*3.141592653589793*radio
# print(f"area: {area}, perimetro: {perimetro}")


# 5) --------[[Pedir segundos e imprimir a cuantas hs equivale]]-----------
# segundos = float(input("Por favor, ingrese segundos: "))
# horas =  segundos/3600
# print(f"{segundos} segundos equivale a {horas} horas!")


# 6) --------[[Pedir numero e imprimir su tabla]]-----------
# n = int(input("Por favor, ingrese un numero para imprimir su tabla: "))
# print(f"{n}x1={n*1}\n{n}x2={n*2}\n{n}x3={n*3}\n{n}x4={n*4}\n{n}x5={n*5}\n{n}x6={n*6}\n{n}x7={n*7}\n{n}x8={n*8}\n{n}x9={n*9}\n{n}x10={n*10}")


# 7) --------[[Pedir 2 numeros y mostrar las 4 operaciones basicas]]-----------
# n1 = float(input("Por favor, ingrese un numero: "))
# n2 = float(input("Por favor, ingrese otro numero: "))

# print(f"{n1} + {n2} = {n1+n2}")
# print(f"{n1} - {n2} = {n1-n2}")
# print(f"{n1} x {n2} = {n1*n2}")
# print(f"{n1} / {n2} = {n1/n2}")


# 8) --------[[calcular el IMC]]-----------
# peso = float(input("Por favor, ingrese su peso: "))
# altura = float(input("Por favor, ingrese su altura en Metros (ej: 1.75): "))
# imc = int(peso // (altura*altura))
# print(F"Su IMC es: {imc}")


# 9) --------[[De Cº a Fº]]-----------
# celcius = int(input("Por favor, ingrese grados celcius: "))
# fahrenheit = ((9/5)*celcius) + 32
# print(F"{celcius} grados celciues son {fahrenheit} fahrenheit")


# 10) --------[[Promiedos]]-----------
n1 = float(input("Por favor, ingrese un numero: "))
n2 = float(input("Por favor, ingrese otro numero: "))
n3 = float(input("Por favor, ingrese otro numero: "))
promedio = (n1+n2+n3) / 3
print(f"El promedioi es: {promedio}")