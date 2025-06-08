def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def fibonacci(p):
    if p== 0:
        return 0
    elif p==1:
        return 1
    else:
        return fibonacci(p-1) + fibonacci(p-2)

def serie_fibonacci(p):
    serie=[]
    for i in range(p+1):
        serie.append(fibonacci(i))
    return serie

def potencia(n, exp):
    if exp==0:
        return 1
    elif exp<0:
        return 1 / potencia(n,-exp)
    else:
        return n * potencia(n,exp-1)
    
def binario(n):
    if n==0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binario(n//2) + str(n%2)
    
def es_palindromo(p):
    if len(p)<=1:
        return True
    if p[0] != p[-1]:
        return False
    return es_palindromo(p[1:-1])

def suma_digitos(n):
    if n<10:
        return n
    else:
        return (n%10) + suma_digitos(n//10)
    
def contar_bloques(n):
    if n==1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
def contar_digito(numero,digito):
    if numero==0:
        return 0
    elif numero%10==digito:
        return 1 + contar_digito(numero//10,digito)
    else:
        return contar_digito(numero//10,digito)
