# 2 listas una con nombres, otra con apellidos
nombres = ["juan", "pedro", "lucas", "julian"]
apellidos = ["morales", "cando", "perez", "rosas"]

# registrar esta información en un txt de forma optima
with open("nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n")
     for n, a in zip(nombres, apellidos)]

# para que el for funcione en una línea debe estar dentro de una lista [], primero el codigo y luego el for