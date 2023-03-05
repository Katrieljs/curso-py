# crear función que devuelva numeros primos
# entre 0 y el argumento que pasamos

def es_primo(num):
    for i in range(2, num-1):  # iniciamos desde el 2
        if num % i == 0:
            return False
    return True


def primos_hasta(num):
    primos = []
    for i in range(3, num+1):  # iniciamos desde 3 hasta el numero que le pasemos
        res = es_primo(i)
        if res == True:
            primos.append(i)
    return primos


primos = primos_hasta(13)
print(primos)
