# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 
# multiplos_4 = list(range(4, 100, 4))
# print(multiplos_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos!
# mi_lista = [1,2,3,'a','b','c']
# print(mi_lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# lista_vacia=[]
# print(lista_vacia)
# lista_vacia.append(1)
# lista_vacia.append(2)
# lista_vacia.append(3)
# print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"] 
# print(animales)
# animales[1]='loro'
# animales[-1]='oso'
# print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:
# Dentro de la lista numero hay distintos valores de tipo entero, a la lista se le aplica el metodo remove que recibe un parametro
# como parametro se le pasa otro metodo que es max que devuelve un valor numerico, ej:
# num_mayor=[1,2,3] - si se llama al metodo max y se pasa num_mayor evalua y devuelve 3, entonces, lo que hace ese fragmento de codigo
# es crear una lista de numero, y elimina el numero mayor, en este caso es el 22.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 
# lista_10_30 = list(range(10,31,5))
# print(lista_10_30[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]
# print(autos)
# autos[1]='bora'
# autos[-2]='vento'
# print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla.
# lista_dobles=[]
# print(lista_dobles)
# lista_dobles.append(5*2)
# lista_dobles.append(10*2)
# lista_dobles.append(15*2)
# print(lista_dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
    # a) Agregar "jugo" a la lista del tercer cliente usando append. 
print(compras)
compras[2].append('jugo')
print(compras)
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1]="tallarines"
print(compras)
    # c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove('pan')
    # d) Imprimir la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla. 
lista_anidadfa=[15, True, [25.5, 57.9, 30.6], False]
print(lista_anidadfa)