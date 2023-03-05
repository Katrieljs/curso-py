# import modulo_saludar as m_saludar
# from modulo_saludar import * # mala practica
from funciones.modulo_saludar import saludar as saludar_normal, saludar_raro

# ahora es un metodo
saludo = saludar_normal("Katriel")
saludo_raro = saludar_raro("Pepe")
print(saludo)
print(saludo_raro)

# para ver las propiedades y metodos de el namespace
# print(dir(m_saludar))

# para ver el nombre del modulo
# print(m_saludar.__name__)
