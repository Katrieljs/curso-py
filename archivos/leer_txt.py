# cuando un archivo se lee hay que cerrarl para volverlo a leer
archivo_sin_leer = open("archivos\\texto.txt", encoding="UTF-8")

# leer archivo completo
# archivo = archivo_sin_leer.read()

# leer linea por linea
#lineas = archivo_sin_leer.readlines()

# leer una sola linea, esta forma puede consumir toda la ram si es un archivo muy grande
# tambien se puede usar un for
linea=archivo_sin_leer.readline() # si no lee la linea completa, lee la cantidad de caracteres que le pasemos

# cerrar archivo
archivo_sin_leer.close()

print(linea)
