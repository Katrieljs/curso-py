# creando diccionario con dict()
# solo así se puede crear diccionarios vacios
diccionario = dict(nombre="Katriel", apellido="Martínez")

# las listas no pueden ser claves, las tuplas si
# usamos frozenset para meter conjuntos

diccionario = {("Katriel", "Martínez"): "jiji"}
diccionario = {frozenset(["Katriel", "Martínez"]): "jiji"}

# creando diccionario con fromkeys()
# da none
# si el primero es iterable el segundo será el valor que se le asigne 
diccionario = dict.fromkeys(["nombre", "apellido"])

print(diccionario)
