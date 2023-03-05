import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\fechas.csv")

valor_mas_alto=df["pedos"].max()
print(valor_mas_alto)

sns.lineplot(x="fecha", y="pedos", data=df)

plt.plot("01-07", valor_mas_alto, "o")

plt.show()
