import pandas as pd

df = pd.read_csv("archivos\\resolviendo_problemas\\datos.csv")

# df[-nombre de la fila-]
# convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

# reemplezar un valor, las veces que aparezca
df["nombre"].replace("Katriel", "Josafat Katriel", inplace=True)

# eliminar filas con datos faltantes
df = df.dropna()

# eliminar las columnas con datos faltantes
df = df.dropna(axis=1)

# eliminar filas repetidas
df = df.drop_duplicates()
print(df)

# creando un csv con el df resultante
df.to_csv("archivos\\resolviendo_problemas\\datos_limpios.csv")
