def calcular_promedio(notas):
    total = 0
    for n in notas:
        total += n

    try:
        promedio = total / len(notas)
    except:
        promedio = 0

    return promedio

def mejor_estudiante(lista):
    mejor = None
    mejor_promedio = 0

    for est in lista:
        promedio = calcular_promedio(est["notas"])
        if promedio > mejor_promedio:
            mejor = est["nombre"]
            mejor_promedio = promedio
    return mejor, mejor_promedio


print("Calculando promedios...\n")

estudiantes = [
    {"nombre": "Ana", "notas": [8, 7, 9]},
    {"nombre": "Luis", "notas": [5, 6]},
    {"nombre": "Marta", "notas": [10, 9, 10]},
    {"nombre": "Pedro", "notas": []}
]

for est in estudiantes:
    print(est["nombre"], "=> promedio:", calcular_promedio(est["notas"]))

nombre, nota = mejor_estudiante(estudiantes)
print(f"\nEl mejor estudiante es {nombre} con una nota media de {nota:.2f}")