import re 

texto='''Hola, holaaaa. esta es la cadena 1. q onda. como vas?
Estas es la segunda línea de texto
esta es la tercera línea de texto 1234 ababababab aababababababab ababab'''

resultado=re.search("Hola", texto)
resultado=re.findall("esta", texto, flags=re.IGNORECASE) #flags, parametros a seguir


# /d -> busca digitos numericos del 0 - 9
resultado=re.findall(r"\d", texto)

# /D -> busca todo menos digitos numericos 
resultado=re.findall(r"\D", texto)

# /w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado=re.findall(r"\w", texto)

# /W -> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado=re.findall(r"\W", texto)

# /s -> busca espacios en blanco
resultado=re.findall(r"\s", texto)

# /S -> busca todo menos espacios en blanco
resultado=re.findall(r"\S", texto)

# . -> busca todo menos saltos en linea 
resultado=re.findall(r".", texto)

# /n -> busca saltos e linea
resultado=re.findall(r"\n", texto)

# / -> cancela caracteres especiales y solo busca el caracter
resultado=re.findall(r"\.", texto)

# armando una cdena que busque un numero, seguido de un punto y un espacio
resultado=re.findall(f'\d\.\s', texto)

# ^ -> busca el comienzo de una linea
# re.M multilinea 
resultado=re.findall(f"^esta", texto, flags=re.M)   

# $ -> busca el final de una linea
# re.M multilinea 
resultado=re.findall(f"texto$", texto, flags=re.M)   

# {n} -> busca n cantidad de veces el valor de la izquierda 
resultado=re.findall(r"\d{3}", texto)

# {n, m} -> rangos 
resultado=re.findall(r"\d{2,4}", texto)

# si encuentra {2} veces ab solo devuelve un ab en caso de {3} igual y así continuemanete
resultado=re.findall(r"(ab){2}", texto)

# | busca una cosa o la otra
resultado=re.findall(r"\d{2,4}|Hola", texto)

print(resultado)