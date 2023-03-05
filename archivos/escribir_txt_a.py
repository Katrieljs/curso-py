with open("archivos\\texto.txt", "a", encoding="UTF-8") as archivo:
    archivo.write(" \n")
    for i in range(5):
        archivo.write(f'Linea {i+1} agregada\n')

# con "a" (append) no sobreescribe, solo agrega
# cada vez que lo abre se ejecuta otra vez, es decir se repite
