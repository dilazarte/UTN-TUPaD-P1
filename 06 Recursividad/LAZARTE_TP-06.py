import data

#1) recursivo numeros factorial
n = int(input("Ingrese un numero para saber su factorial: "))
fact=data.factorial(n)
print(f"El factorial de {n} es {fact}")

#2) recursivo fibonacci (serie)
n = int(input("Ingrese un numero para fibonacci: "))
print(data.serie_fibonacci(n)) #no lo hago con print ya que la funcion tiene un print interno.

#3) funcion recursiva exponente
n = int(input("Ingrese un numero: "))
exp = int(input("Ingrese un exponente: "))

print(f"{n} a la {exp} es {data.potencia(n, exp)}")

#4) decimal a binario
n = int(input("Ingrese un numero: "))
nBin = data.binario(n)
print(nBin)

#5) palabra palindromo
p = (input("Ingrese una palabra para ver si es palindromo: "))
print(data.es_palindromo(p))

#6) sumar digitos
n = int(input("Ingrese un numero para sumar sus digits: "))
print(data.suma_digitos(n))

#7) contar los bloques
n = int(input("Ingrese un numero para contrar los bloques: "))
print(data.contar_bloques(n))

#8) contar digitos en numeros
n = int(input("Ingrese un numero: "))
d = int(input("Ingrese el digito (del 0 al 9) para ver cuanta veces se repite: "))

print(f"En el numero {n} el digito {d} se repite {data.contar_digito(n,d)} veces!")