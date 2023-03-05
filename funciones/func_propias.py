# función simple
def saludar():
    print("Holaaaa")


saludar()

# función con parametros


def saludar_usuario(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = "amor"
    print(f'Holaaaa {nombre}, cómo estas mi {adjetivo}')


saludar_usuario("Julian", "nose")
saludar_usuario("Julia", "mujer")
saludar_usuario("Pablo", "hombre")

# crear una funcion que devuelva valores


def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c_1 = num-2
    c_2 = num
    c_3 = num-5
    contraseña = f'{chars[c_1]}{chars[c_2]}{chars[c_3]}{num*2}'
    return contraseña, num


password, primer_num = crear_contraseña_random(89329)
frase = f'Tu contraseña nueva es: {password}'
print(frase)
print(f'El numero utilizado para crearla fue: {primer_num}')
