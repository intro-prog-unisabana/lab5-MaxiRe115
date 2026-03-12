def promedio_estudiante(calificaciones):
    if len(notas) == 0:
        return 0.0
    return sum(calificaciones) / len(calificaciones)
notas= [85, 92, 78]
promedio= promedio_estudiante(notas)
print(promedio)
