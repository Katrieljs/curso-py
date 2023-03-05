def sumar_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            res = int(a)+int(b)
        except Exception as e:
            print("Pedí un numero")
            print(f'Error: {e}')
        else:
            break
        finally:
            print("Esto se ejecuta siempre sin importar lo que pase")
    return res


print(sumar_dos())
