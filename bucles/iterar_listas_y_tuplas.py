# python usa for in

animales = ["perro", "gato", "vaca", "cocodrilo"]
numeros = [1, 2, 3, 4]

for animal in animales:
    if animal.endswith("a"):
        conector = "una"
    else:
        conector = "un"
    print(f'Ahora el animal es {conector} {animal}')

# recorrer dos listas
for numero, animal in zip(numeros, animales):
    print(f'El animal numero {numero} es {animal}')

print("-----------")

# iterar con range
# el primero esta incluido y el ultimo no
for num in range(5, 10):
    print(num)

print("-----------")

# forma no optima
for num in range(len(numeros)):
    print(numeros[num])

print("-----------")

# forma correcta enumerate y te permite obtener el indice
# devuelve tuplas, el primer elemento es el indice y el segundo es el valor
for num in enumerate(numeros):
    print(num[1])

print("-----------")


# usando el else

for numero in numeros:
    print(f'Ejecutando el ultimo, valor actual: {numero}')
else:
    print("El bucle termino")

# todo lo anterior sirve para tuplas