def frase(nombre, apellido, adjetivo="pequeño"):
    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'


frase_1 = frase(apellido="Martínez", adjetivo="pro", nombre="Katriel")
print(frase_1)
