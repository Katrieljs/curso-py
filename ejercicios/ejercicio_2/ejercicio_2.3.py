# creando un fibonacci entre el 0 y el número dado

def fibonacci(num):
    a, b = 0, 1 
    lista_fibonacci = []
    for i in range(num):
        if b > num:
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a, b = b, a+b

res = fibonacci(21)
print(res)
