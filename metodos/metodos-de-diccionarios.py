diccionario = {
    "nombre": "Katriel",
    "apellido": "Martínez",
    "edad": 16
}

# devuelve las key o valores clave y sirve para iterar
claves = diccionario.keys()

# devuelve el valor de la clave, si no lo encuetra devuelve none
valor = diccionario.get("nombre")

# tambien podemos hacer eso pero si no lo encuentra da un error
print(diccionario["edad"])

#elimina todos los elementos de un diccionario
#dicionario.clear()

print(valor)
