# con set()
# no se puede poner elementos mutables dentro del set
conjunto = set(["dato_1", "dato_2"])

# metiendo un conjunto dentro de otro conjunto con frozenset()
conjunto_1 = frozenset(["dato_1", "dato_2"])
conjunto_2 = {conjunto_1, "dato_3"}

print(conjunto_2)

# teoría de conjuntos

conjunto_1 = {1, 3, 5, 7}
conjunto_2 = {1, 3, 7}

# detectar si es un subconjunto con issubset()
res = conjunto_2.issubset(conjunto_1)
# detectar si es un subconjunto con <=
res = conjunto_2 <= conjunto_1

# detectar si es un superconjunto con issuperset()
res = conjunto_1.issuperset(conjunto_2)
# detectar si es un superconjunto con >=
res = conjunto_1 > conjunto_2

# verificar si hay un elemento en comun
res=conjunto_1.isdisjoint(conjunto_2)

print(res)
