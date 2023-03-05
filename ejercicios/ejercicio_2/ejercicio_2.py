# falto el porfesor y los alumnos van a dar la clase
# pedir nombre y edad de los alumnos

def obtener_compañeros(cantidad_de_compañeros):
    compañeros=[]
    for i in range(cantidad_de_compañeros):
        nombre=input("Ingrese el nombre del compañero ")
        edad=int(input("Ingrese la edad del compañero "))
        compañero=(nombre, edad) # tupla [0]=nombre [1]=edad
        compañeros.append(compañero) # añade tuplas a la lista [(1,2), (1,2), (1,2)]
    compañeros.sort(key=lambda x:x[1]) # ordena con sort, usa la edad [1]
    asistente=compañeros[0][0]
    profesor=compañeros[-1][0]
    return asistente, profesor

asistente, profesor=obtener_compañeros(5)
print(f'El profesor es: {profesor} y su asistente es: {asistente}')
    

    