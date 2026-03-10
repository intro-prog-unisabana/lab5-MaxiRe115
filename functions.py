def promedio_estudiante(*calificaciones):
    if len(notas) == 0:
        return 0.0
    suma= sum(calificaciones)
    prom= suma / len(calificaciones)
    return float(prom)
notas= []
promedio= promedio_estudiante(notas)
print(promedio)
