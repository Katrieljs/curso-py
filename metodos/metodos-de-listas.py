lista=list(["hola", "soy", "yo"])

#numero de elementos
res=len(lista)

#agregar elementos a la lista con append (llamamos a la lista, no crea una nueva solo la modifica)
lista.append("jiji")

#agredar elementos a la lista en un indice especifico
lista.insert(1, "a")

#agregamos varios elementos
lista.extend(["lalala", 30])

#eliminamos un elementos de la lista por su indice
lista.pop(-1)

#remueve un elemento por su valor, si no encuentra el elemento lanza un error
lista.remove("a")

#ordena los elementos de forma ascendente (solo numeros o solo texto)
lista.sort()

#revierte todo, osea desciende 
lista.sort(reverse=True)

#la revierte
lista.reverse()

#elimina todo los elementos de la lista
#lista.clear()

print(lista)