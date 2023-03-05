frase = input(
    "Dime una frase y te calclo cuanto tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print("Tampoco te pedí un testamento")

print(
    f'Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos')
print(f'Dalto tardaria {cantidad_de_palabras//2/1.3} segundos en decirlo')


