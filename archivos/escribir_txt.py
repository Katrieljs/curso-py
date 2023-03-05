with open("archivos\\texto.txt", "w", encoding="UTF-8") as archivo:
    # archivo.write("que, so")
    # escribe las lineas con una lista
    archivo.writelines(["escribe\n", "escribe otra vez\n"])
    archivo.writelines(["x2\n", "sobre escribe una vez, luego apila\n"])
# "w" es write nos permite escribir en el archivo
# .write() sobre escribe el archivo
