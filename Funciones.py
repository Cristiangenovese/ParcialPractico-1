import Inputs

# Listas paralelas para almacenar los datos de los participantes
nombres = []
puntajes_j1 = []
puntajes_j2 = []
puntajes_j3 = []
promedios = []
CANT_PARTICIPANTES = 0

def cargar_participantes(cantidad_participantes: int) -> bool:
    '''
    Carga los nombres de los participantes y reinicia las listas de puntajes y promedios.

    Args:
        cantidad_participantes (int): La cantidad total de participantes.

    Returns:
        bool: True si la carga fue exitosa.
    '''
    global nombres, puntajes_j1, puntajes_j2, puntajes_j3, promedios, CANT_PARTICIPANTES
    CANT_PARTICIPANTES = cantidad_participantes
    nombres = [""] * cantidad_participantes
    puntajes_j1 = [0] * cantidad_participantes
    puntajes_j2 = [0] * cantidad_participantes
    puntajes_j3 = [0] * cantidad_participantes
    promedios = [0.0] * cantidad_participantes

    for i in range(CANT_PARTICIPANTES):
        print(f"\nCargando participante {i + 1} de {CANT_PARTICIPANTES}:")
        nombres[i] = Inputs.validar_nombre()

    print("\nParticipantes cargados correctamente.")
    return True

def cargar_puntuaciones() -> bool:
    '''
    Carga las puntuaciones de los 3 jurados para cada participante y calcula su promedio.

    Returns:
        bool: True si la carga fue exitosa, False si no hay participantes cargados.
    '''
    if CANT_PARTICIPANTES == 0 or nombres[0] == "":
        print("Primero debe cargar los participantes.")
        return False

    for i in range(CANT_PARTICIPANTES):
        print(f"\nCargando puntajes para {nombres[i]}:")
        puntajes_j1[i] = Inputs.validar_puntaje(1)
        puntajes_j2[i] = Inputs.validar_puntaje(2)
        puntajes_j3[i] = Inputs.validar_puntaje(3)
        promedios[i] = (puntajes_j1[i] + puntajes_j2[i] + puntajes_j3[i]) / 3

    print("\nPuntuaciones cargadas correctamente.")
    return True

def mostrar_puntuaciones() -> None:
    '''
    Muestra el nombre, los puntajes y el promedio de cada participante.
    '''
    print("\n-- Puntuaciones --")
    for i in range(CANT_PARTICIPANTES):
        print(f"Nombre: {nombres[i]}")
        print(f"Puntajes: [{puntajes_j1[i]}, {puntajes_j2[i]}, {puntajes_j3[i]}]")
        print(f"Promedio: {promedios[i]:.2f}")
        print("-" * 30)

def participantes_promedio_menor_4() -> None:
    '''
    Muestra los participantes con promedio menor a 4.
    '''
    encontrados = False
    for i in range(CANT_PARTICIPANTES):
        if promedios[i] < 4:
            if not encontrados:
                print("\n-- Participantes con promedio menor a 4 --")
            print(f"{nombres[i]} - Promedio: {promedios[i]:.2f}")
            encontrados = True
    if not encontrados:
        print("No hay participantes con promedio menor a 4.")

def participantes_promedio_menor_8() -> None:
    '''
    Muestra los participantes con promedio menor a 8.
    '''
    encontrados = False
    for i in range(CANT_PARTICIPANTES):
        if promedios[i] < 8:
            if not encontrados:
                print("\n-- Participantes con promedio menor a 8 --")
            print(f"{nombres[i]} - Promedio: {promedios[i]:.2f}")
            encontrados = True
    if not encontrados:
        print("No hay participantes con promedio menor a 8.")

def promedio_por_jurado() -> None:
    '''
    Calcula y muestra el promedio de cada jurado.
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(CANT_PARTICIPANTES):
        suma_j1 += puntajes_j1[i]
        suma_j2 += puntajes_j2[i]
        suma_j3 += puntajes_j3[i]

    print("\n-- Promedio por Jurado --")
    print(f"Jurado 1: {suma_j1 / CANT_PARTICIPANTES:.2f}")
    print(f"Jurado 2: {suma_j2 / CANT_PARTICIPANTES:.2f}")
    print(f"Jurado 3: {suma_j3 / CANT_PARTICIPANTES:.2f}")


def jurado_mas_estricto() -> None:
    '''
    Muestra el jurado con el promedio más bajo.
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(CANT_PARTICIPANTES):
        suma_j1 += puntajes_j1[i]
        suma_j2 += puntajes_j2[i]
        suma_j3 += puntajes_j3[i]

    promedios_j = [
        suma_j1 / CANT_PARTICIPANTES,
        suma_j2 / CANT_PARTICIPANTES,
        suma_j3 / CANT_PARTICIPANTES
    ]

    min_prom = promedios_j[0]
    for prom in promedios_j:
        if prom < min_prom:
            min_prom = prom

    print("\n-- Jurado más estricto --")
    for i in range(3):
        if promedios_j[i] == min_prom:
            print(f"Jurado {i + 1} con promedio {min_prom:.2f}")

def jurado_mas_generoso() -> None:
    '''
    Muestra el jurado con el promedio más alto.
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(CANT_PARTICIPANTES):
        suma_j1 += puntajes_j1[i]
        suma_j2 += puntajes_j2[i]
        suma_j3 += puntajes_j3[i]

    promedios_j = [
        suma_j1 / CANT_PARTICIPANTES,
        suma_j2 / CANT_PARTICIPANTES,
        suma_j3 / CANT_PARTICIPANTES
    ]

    max_prom = promedios_j[0]
    for prom in promedios_j:
        if prom > max_prom:
            max_prom = prom

    print("\n-- Jurado más generoso --")
    for i in range(3):
        if promedios_j[i] == max_prom:
            print(f"Jurado {i + 1} con promedio {max_prom:.2f}")


def participantes_puntajes_iguales() -> None:
    '''
    Muestra los participantes que recibieron los mismos puntajes en los 3 jurados.
    '''
    encontrados = False
    for i in range(CANT_PARTICIPANTES):
        if puntajes_j1[i] == puntajes_j2[i] == puntajes_j3[i]:
            if not encontrados:
                print("\n-- Participantes con puntajes iguales --")
            print(f"{nombres[i]} - Puntajes: [{puntajes_j1[i]}, {puntajes_j2[i]}, {puntajes_j3[i]}]")
            encontrados = True
    if not encontrados:
        print("No hay participantes con puntajes iguales.")

def comparar_strings_ignorando_mayusculas(a: str, b: str) -> bool:
    '''
    Compara dos strings carácter por carácter ignorando mayúsculas/minúsculas.
    '''
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        char_a = a[i]
        char_b = b[i]

        # Convertir a minúscula si es mayúscula (A-Z)
        if 'A' <= char_a <= 'Z':
            char_a = chr(ord(char_a) + 32)
        if 'A' <= char_b <= 'Z':
            char_b = chr(ord(char_b) + 32)

        if char_a != char_b:
            return False

    return True

def buscar_participante() -> None:
    '''
    Busca un participante por nombre e imprime sus datos.
    '''
    nombre = Inputs.confirmar_busqueda()
    encontrado = False
    for i in range(CANT_PARTICIPANTES):
        if comparar_strings_ignorando_mayusculas(nombres[i], nombre):
            print(f"Nombre: {nombres[i]}")
            print(f"Puntajes: [{puntajes_j1[i]}, {puntajes_j2[i]}, {puntajes_j3[i]}]")
            print(f"Promedio: {promedios[i]:.2f}")
            encontrado = True
            break
    if not encontrado:
        print("Participante no encontrado.")

def top3_participantes() -> None:
    '''
    Muestra los 3 participantes con mayor promedio.
    '''
    print("\n-- Top 3 Participantes --")
    indices = list(range(CANT_PARTICIPANTES))
    for i in range(CANT_PARTICIPANTES):
        for j in range(CANT_PARTICIPANTES - i - 1):
            if promedios[indices[j]] < promedios[indices[j + 1]]:
                indices[j], indices[j + 1] = indices[j + 1], indices[j]
    for i in range(min(3, CANT_PARTICIPANTES)):
        print(f"{nombres[indices[i]]} - Promedio: {promedios[indices[i]]:.2f}")

def participantes_ordenados() -> None:
    '''
    Muestra los participantes ordenados alfabéticamente con sus datos.
    '''
    print("\n-- Participantes Ordenados Alfabéticamente --")
    indices = list(range(CANT_PARTICIPANTES))
    for i in range(CANT_PARTICIPANTES):
        for j in range(CANT_PARTICIPANTES - i - 1):
            if nombres[indices[j]].lower() > nombres[indices[j + 1]].lower():
                indices[j], indices[j + 1] = indices[j + 1], indices[j]
    for i in indices:
        print(f"{nombres[i]} - Puntajes: [{puntajes_j1[i]}, {puntajes_j2[i]}, {puntajes_j3[i]}] - Promedio: {promedios[i]:.2f}")