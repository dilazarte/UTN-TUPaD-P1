import data

##Implementacion de las funciones:

#creamos el arbol de prueba (Nodo raiz A)
arbol_prueba = data.crearArbol('A')

#agregamos 2 hijos, nodos B y C
data.insertarIzquierda(arbol_prueba, "B")
data.insertarDerecha(arbol_prueba, "C")

#agregamos 2 hijos pero al nodo B (izquierdo) en este casos los D y E
data.insertarIzquierda(arbol_prueba[1], "D") 
data.insertarDerecha(arbol_prueba[1], "E")


##Recorremos:
print("Recorrido Preorden:")
data.recPreorden(arbol_prueba)
#la salida deberia ser: A B D E C

print("\nRecorrido Inorden:")
data.recInorden(arbol_prueba)
#la salida deberia ser: D B E A C

print("\nRecorrido Postorden:")
data.recPostorden(arbol_prueba)
#la salida deberia ser: D E B C A

