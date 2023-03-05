# froma no optima de sumar valores
#def suma(lista):
#    numeros_sumados=0
#    for numero in lista:
#        numeros_sumados+=numeros_sumados+numero
#    return numeros_sumados

# con *args 
def suma(nombre, *numeros):
    return f'El nombre es {nombre} y la suma es {sum(numeros)}'

res = suma("Katriel",5,2,5)
print(res)
