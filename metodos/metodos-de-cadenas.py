cadena_1 = "Hola soy yo"
cadena_2 = "Jijijij ptyhon"

#lo pone en mayusculas
res=cadena_1.upper() 

#lo pone en minusculas
res=cadena_1.lower() 

#primera letra en mayuscula
res=cadena_1.capitalize()

#buscamos una cadena en otra cadena, si no la encuentra devuelve -1
res=cadena_1.find("Hola")

#buscamos una cadena en otra cadena, si no encuentra devuelve un error
res=cadena_1.index("Hola")

#si es numerico devuelve true, puede ser texto de numeros o numeros
res=cadena_1.isnumeric()

#si es alfanumerico devuelve true, solo es balido los caracteres de la a-z (los espacios no cuentan)
res=cadena_1.isalpha()

#cuenta coincidencias
res=cadena_1.count("o")

#contar caracteres
res=len(cadena_1)

#verificamos si una cadena empieza con otra cadena dada
res=cadena_1.startswith("Hola")

#verificamos si una cadena termina con tra cadena
res=cadena_1.endswith("yo")

#reemplaza un pedazo de cadena con otra dada
res=cadena_1.replace("o", "u")

#separar cadenas, devuevle una matriz

res=cadena_1.split(" ")

print(res)
