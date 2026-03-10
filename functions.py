def promedio_estudiante(*calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    for num in calificaciones:
        suma= sum(calificaciones)
        prom= suma / len(calificaciones)
        return float(prom)
promedio= promedio_estudiante(85, 92, 78)
print(promedio)
