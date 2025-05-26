import utiles ##traigo las funciones de otro modulo

# 1)------------
print(utiles.imprimir_hola_mundo())

# 2)------------
print(utiles.saludar_usuario("David"))

# 3)------------

print(utiles.informacion_personal("David", "Lazarte",80, "Cordoba"))

# 4)------------
radio = int(input("Ingrese el radio de un circulo por favor:\n"))
area = utiles.calcular_area_circulo(5)
perimetro = utiles.calcular_perimetro_circulo(5)
print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

# 5)------------
seg = int(input("Ingrese los segundos para saber su equivalente en horas:\n"))
hs = utiles.segundos_a_horas(seg)
print(f"{seg} a horas son: {hs}")

# 6)------------
numero_tabla = int(input("Ingrese numero para ver su tabla:\n"))
utiles.tabla_multiplicar(numero_tabla)

# 7)------------
numero_uno = int(input("Ingrese numero por favor:\n"))
numero_dos = int(input("Ingrese otro numero:\n"))
data=utiles.operaciones_basicas(numero_uno, numero_dos)

print(f"Suma: {data[0]}, resta: {data[1]}, multuplicacion: {data[2]}, division: {data[3]}")

# 8)------------
peso = int(input("Ingrese su peso por favor:\n"))
altura = int(input("Ingrese su altura en metros por favor:\n"))
imc = utiles.calcular_imc(peso, altura)
print(f"Su IMC es {imc}")

# 9)------------
c = utiles.celsius_a_fahrenheit(55)
print(c)

# 10)------------
promdio = utiles.calcular_promedio(5,5,5)
print(promdio)