
frutas = ["manzana", "pera", "piña", "ciruela", "mango", "naranja", "maracuya"]
cadena = "Holaaa *dice algo*"
numeros = [1, 3, 5, 8]

# sentencia continue
for fruta in frutas:
    if fruta == "ciruela":
        continue
    print(f'Me voy a comer una {fruta}')

print("----------------------")

# evitar que un bucle siga con break (el else tampoco se ejecuta)
for fruta in frutas:
    if fruta == "ciruela":
        break
    print(f'Me voy a comer una {fruta}')

else:
    print("terminado")

print("----------------------")
# recorrer una cadena de texto

for letra in cadena:
    print(letra)

print("----------------------")
# for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)
