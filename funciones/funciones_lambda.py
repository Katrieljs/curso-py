numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# como una función flecha
# es una función anonima
# funcion con lambda para muriplicar por dos


def multiplicar_por_dos(x): return x*2


print(multiplicar_por_dos(5))

# funcion para saber pares


def es_par(num):
    if (num % 2 == 0):
        return True


# usando filter con una función comun
# como un bucle artificial
# usa la función
# usa cada uno de los elementos de la lista para pasarselos a la función
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# lo mismo pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares))
