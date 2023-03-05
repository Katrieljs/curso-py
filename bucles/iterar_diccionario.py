diccionario = {
    "nombre": "Katriel",
    "apellido": "Martínez",
    "edad": 16
}

# devuelve una tupla con par clave-valor
for key in diccionario.items():
    print(key)

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es {key} y el valor es {value}')
