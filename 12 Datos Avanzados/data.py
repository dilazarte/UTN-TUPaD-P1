def crearArbol(nombreNodoRaiz):
	return [nombreNodoRaiz, [], []]
    
    
def insertarIzquierda(arbol, nuevoValor):
    subarbolIzq = arbol[1]
    if subarbolIzq:
        arbol[1] = [nuevoValor, subarbolIzq, []]
    else:
        arbol[1] = [nuevoValor, [], []]

def insertarDerecha(arbol, nuevoValor):
    subarbolDer = arbol[2]
    if subarbolDer:
        arbol[2] = [nuevoValor, [], subarbolDer]
    else:
        arbol[2] = [nuevoValor, [], []]
        
        
def recPreorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        recPreorden(arbol[1])
        recPreorden(arbol[2])
        
def recInorden(arbol):
    if arbol:
        recInorden(arbol[1])
        print(arbol[0], end=' ')
        recInorden(arbol[2])

def recPostorden(arbol):
    if arbol:
        recPostorden(arbol[1])
        recPostorden(arbol[2])
        print(arbol[0], end=' ')