def promedio_estudiante(calificaciones):
    if len(notas) == 0:
        return 0.0
    return float(sum(calificaciones) / len(calificaciones))
notas= []
promedio= promedio_estudiante(notas)
print(promedio)
