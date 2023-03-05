import pandas as pd

# df, data frame son estructuras de datos bidimensionales
# filas y columnas, como una hoja de calculo

# con names podemos cambiar los encabezados names=["name", "lastname", "age"]
# names=["name", "lastname", "age"] pasaría a ser un encabezado
# nombre apellido y edad pasaría a ser la primera fila osea la fila[0]
df = pd.read_csv("archivos\\datos.csv")
df_2 = pd.read_csv("archivos\\datos.csv")

# datos de la columno "nombre"
print(df["nombre"])
print("-------------")

# ordenar el dataframe por edad
# crea un valor anonimo hay que guardarlo en una variable
df_ordenado = df.sort_values("edad")
print(df_ordenado)
print("-------------")

# ordenando la edad de forma descendente
df_ordenado_desc = df.sort_values("edad", ascending=False)
print(df_ordenado_desc)
print("-------------")

# concatenando df
df_concatenado=pd.concat([df, df_2])
print(df_concatenado)
print("-------------")

# accediendo a las primeras 2 filas con head()
primeras_filas=df.head(2)
print(primeras_filas)
print("-------------")

# accediendo a las ultimas 2 filas con tail()
ultumas_filas=df.tail(2)
print(ultumas_filas)
print("-------------")

# accediendo a la cantidad de filas y culumnas con shape
# devuelve una tupla
filas_y_culumnas=df.shape
filas_totales,columnas_totales=df.shape

print(filas_y_culumnas)
print(filas_totales)
print(columnas_totales)
print("-------------")

# obteniendo datos estadisticos del df
df_info=df.describe()
print(df_info)
print("-------------")

# accediendo a un elemento especifico del df con loc
# primer parametro fila, segundo, columna
elemento_especifico_loc=df.loc[2, "edad"]
# o con iloc
elemento_especifico_loc=df.iloc[2, 2]
print(elemento_especifico_loc)
print("-------------")

# accediendo a todas las filas de una columna
apellidos=df.iloc[:,1]
print(apellidos)
print("-------------")

# accediendo a la fila 3 con iloc y loc
fila_3=df.iloc[2,:]
print(fila_3)
print("-------------")

# accediendo a filas con edad mayor a 10
mayor_que_10=df.loc[df["edad"]>10,:]
print(mayor_que_10)
print("-------------")


# slicing inicio:final
# el ultimo no se encuentra incluido
cadena = "0123456789"
print(cadena[:3])
