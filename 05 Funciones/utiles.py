from math import pi

# 1)------------
def imprimir_hola_mundo():
    return "Hola Mundo!"

# 2)------------
def saludar_usuario(nombre) :
    return f"Hola {nombre}!"

# 3)------------
def informacion_personal(nombre, apellido, edad, ciudad):
    return f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}"

# 4)------------
def calcular_area_circulo(radio): #esto era pi*radio*radio
    return round(pi*radio*radio, 2)

def calcular_perimetro_circulo(radio): #aca era 2*pi*radio
    return round(2*pi*radio, 2)

# 5)------------
def segundos_a_horas(segundos): # una hora eran 3600 segundos
    return round(segundos/3600, 2)

# 6)------------
def tabla_multiplicar(numero):
    for i in range(1,11) :
        print(f"{numero} x {i} = {i*numero}")

# 7)------------
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    if b != 0 :
        division = a / b
    else :
        division = "No se puede dividir por 0 (cero)"
    return (suma, resta, producto, division)

# 8)------------
def calcular_imc(peso, altura):
    if altura <= 0:
        return "La altura no puede ser 0 (cero)"
    return peso / (altura * altura)

# 9)------------
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10)------------
def calcular_promedio(a, b, c):
    return round((a+b+c) / 3, 2)