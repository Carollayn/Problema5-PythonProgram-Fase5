# NOMBRE: CAROLLAYN HERRERA RAMIREZ
# DOCUMENTO: 1005095082
# PROGRAMA: CONTROL DE HORAS SEMANALES
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN

# Matriz con los recursos y horas trabajadas
recursos = [
    ["Ana", 8, 8, 9, 8, 10],
    ["Carlos", 7, 8, 8, 7, 8],
    ["Luisa", 9, 9, 8, 9, 9],
    ["Pedro", 6, 7, 8, 7, 6]
]

# Función para clasificar la jornada laboral

def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

# Recorrido de la matriz

print("========== REPORTE SEMANAL ==========\n")

for recurso in recursos:

    try:
        # Obtener nombre
        nombre = recurso[0]

        # Validar nombre vacío
        if nombre.strip() == "":
            print("Error: nombre inválido\n")
            continue

        # Obtener horas trabajadas
        horas = recurso[1:]

        # Validar que todos los datos sean numéricos
        for hora in horas:
            if not isinstance(hora, (int, float)):
                raise ValueError("Error: dato inválido")

        # Validar horas negativas
        for hora in horas:
            if hora < 0:
                raise ValueError("Error: existen horas inválidas")

        # Calcular total de horas
        total_horas = sum(horas)

        # Clasificar jornada
        clasificacion = clasificar_jornada(total_horas)

        # Mostrar resultados
        print(f"Recurso: {nombre}")
        print(f"Total de horas: {total_horas}")
        print(f"Clasificación: {clasificacion}")
        print("-----------------------------------")

    except ValueError as error:
        print(error)