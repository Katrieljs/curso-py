
# duraciones en promedio
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

# duracion de curdo
crudo_prom = 5
crudo_dalto = 3.5

# diferencias de duración
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_prom = 100 - dalto_curso / otros_cursos_prom * 100

print("----------------------------------")
print("El curso de Dalto dura: ")
print(
    f'  -un {int(diferencias_con_min)}% menos que el más rapido')
print(
    f'  -un {diferencias_con_max}% menos que el más lento')
print(
    f'  -un {diferencias_con_prom}% menos que el promedio')
print("----------------------------------")


# Porcentaje de tiempo vacio removido
tiempo_vacio_prom = 100 - otros_cursos_prom * 1000 // crudo_prom / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print(f'Un curso pormedio elimina un {tiempo_vacio_prom}% de tiempo vacio')
print(f'El curso de Dalto elimino un {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------------------------")


# Mostrando diferencias si los cursos duraran 10 horas
print(
    f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom*100//dalto_curso/10} horas de otros cursos')
print(
    f'Ver 10 horas de otros curso equivale a ver {dalto_curso*100//otros_cursos_prom/10} horas de otros cursos')
print("----------------------------------")
