#ejercicio que determine si un alumno esta aprobado
#autor: Elias Gomez Flores



def determinaraprobado(promedio):
    if promedio>=11:
        resultado="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado

print(determinaraprobado(15))




