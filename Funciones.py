import Inputs

def mostrar_puntuaciones(participantes: list, cantidad_participantes: int) -> list:
    '''
    Obtiene los datos de cada participante para mostrar.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de tuplas (nombre, puntaje1, puntaje2, puntaje3, promedio).
    '''
    datos = [("", 0, 0, 0, 0.0)] * cantidad_participantes  # Lista inicializada

    for i in range(cantidad_participantes):
        nombre = participantes[i][0]
        p1 = participantes[i][1]
        p2 = participantes[i][2]
        p3 = participantes[i][3]
        promedio = participantes[i][4]

        datos[i] = (nombre, p1, p2, p3, promedio)

    return datos


def participantes_promedio_menor_4(participantes: list, cantidad_participantes: int) -> list:
    '''
    Obtiene los participantes con promedio menor a 4.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de tuplas (nombre, promedio) de participantes con promedio menor a 4.
    '''
    resultados = [("", 0.0)] * cantidad_participantes  # Lista inicializada
    contador = 0  # Contador para saber cuántos cumplen la condición

    for i in range(cantidad_participantes):
        if participantes[i][4] < 4:
            resultados[contador] = (participantes[i][0], participantes[i][4])
            contador += 1

    # Recortar la lista a la cantidad real de resultados
    lista_final = [("", 0.0)] * contador
    for i in range(contador):
        lista_final[i] = resultados[i]

    return lista_final

def participantes_promedio_menor_8(participantes: list, cantidad_participantes: int) -> list:
    '''
    Obtiene los participantes con promedio menor a 8.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de tuplas (nombre, promedio) de participantes con promedio menor a 8.
    '''
    resultados = [("", 0.0)] * cantidad_participantes
    contador = 0

    for i in range(cantidad_participantes):
        if participantes[i][4] < 8:
            resultados[contador] = (participantes[i][0], participantes[i][4])
            contador += 1

    lista_final = [("", 0.0)] * contador
    for i in range(contador):
        lista_final[i] = resultados[i]

    return lista_final


def promedio_por_jurado(participantes: list, cantidad_participantes: int) -> list:
    '''
    Calcula el promedio de puntuaciones otorgadas por cada jurado.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista con el promedio de cada jurado [promedio_j1, promedio_j2, promedio_j3].
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(cantidad_participantes):
        suma_j1 += participantes[i][1]
        suma_j2 += participantes[i][2]
        suma_j3 += participantes[i][3]

    promedio_j1 = suma_j1 / cantidad_participantes
    promedio_j2 = suma_j2 / cantidad_participantes
    promedio_j3 = suma_j3 / cantidad_participantes

    return [promedio_j1, promedio_j2, promedio_j3]


def jurado_mas_estricto(participantes: list, cantidad_participantes: int) -> list:
    '''
    Determina qué jurado(s) tiene el promedio más bajo.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista con el/los número(s) de jurado(s) más estricto(s) (1, 2 o 3).
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(cantidad_participantes):
        suma_j1 += participantes[i][1]
        suma_j2 += participantes[i][2]
        suma_j3 += participantes[i][3]

    promedio_j1 = suma_j1 / cantidad_participantes
    promedio_j2 = suma_j2 / cantidad_participantes
    promedio_j3 = suma_j3 / cantidad_participantes

    # Buscamos el menor promedio
    menor = promedio_j1
    if promedio_j2 < menor:
        menor = promedio_j2
    if promedio_j3 < menor:
        menor = promedio_j3

    jurados_estrictos = [0, 0, 0]  # 0: no es estricto, 1: es estricto
    if promedio_j1 == menor:
        jurados_estrictos[0] = 1
    if promedio_j2 == menor:
        jurados_estrictos[1] = 1
    if promedio_j3 == menor:
        jurados_estrictos[2] = 1

    resultado = [0] * 3  # como máximo pueden ser los 3 jurados
    contador = 0
    for i in range(3):
        if jurados_estrictos[i] == 1:
            resultado[contador] = i + 1  # Jurado 1, 2 o 3
            contador += 1

    jurados_final = [0] * contador
    for i in range(contador):
        jurados_final[i] = resultado[i]

    return jurados_final


def jurado_mas_generoso(participantes: list, cantidad_participantes: int) -> list:
    '''
    Determina qué jurado(s) tiene el promedio más alto.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista con el/los número(s) de jurado(s) más generoso(s) (1, 2 o 3).
    '''
    suma_j1 = 0
    suma_j2 = 0
    suma_j3 = 0

    for i in range(cantidad_participantes):
        suma_j1 += participantes[i][1]
        suma_j2 += participantes[i][2]
        suma_j3 += participantes[i][3]

    promedio_j1 = suma_j1 / cantidad_participantes
    promedio_j2 = suma_j2 / cantidad_participantes
    promedio_j3 = suma_j3 / cantidad_participantes

    # Buscar el mayor promedio
    mayor = promedio_j1
    if promedio_j2 > mayor:
        mayor = promedio_j2
    if promedio_j3 > mayor:
        mayor = promedio_j3

    jurados_generosos = [0, 0, 0]  # 0: no es generoso, 1: es generoso
    if promedio_j1 == mayor:
        jurados_generosos[0] = 1
    if promedio_j2 == mayor:
        jurados_generosos[1] = 1
    if promedio_j3 == mayor:
        jurados_generosos[2] = 1

    resultado = [0] * 3  # como máximo pueden ser los 3 jurados
    contador = 0
    for i in range(3):
        if jurados_generosos[i] == 1:
            resultado[contador] = i + 1  # Jurado 1, 2 o 3
            contador += 1

    jurados_final = [0] * contador
    for i in range(contador):
        jurados_final[i] = resultado[i]

    return jurados_final


def participantes_puntajes_iguales(participantes: list, cantidad_participantes: int) -> list:
    '''
    Devuelve los participantes que tienen la misma puntuación en los tres jurados.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de nombres de participantes con puntajes iguales en los tres jurados.
    '''
    resultados = [""] * cantidad_participantes
    contador = 0

    for i in range(cantidad_participantes):
        p1 = participantes[i][1]
        p2 = participantes[i][2]
        p3 = participantes[i][3]

        if p1 == p2 and p2 == p3:
            resultados[contador] = participantes[i][0]
            contador += 1

    final = [""] * contador
    for i in range(contador):
        final[i] = resultados[i]

    return final


def comparar_strings_ignorando_mayusculas(a: str, b: str) -> bool:
    # Función auxiliar para comparar strings sin distinguir mayúsculas/minúsculas.
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        char_a = a[i]
        char_b = b[i]

        if 'A' <= char_a <= 'Z':
                char_a = chr(ord(char_a) + 32)
        if 'A' <= char_b <= 'Z':
                char_b = chr(ord(char_b) + 32)

        if char_a != char_b:
            return False

    return True


def buscar_participante(participantes: list, cantidad_participantes: int, nombre_buscado: str) -> tuple or None:
    # Función para buscar participante (usando la función auxiliar).
    for i in range(cantidad_participantes):
        if comparar_strings_ignorando_mayusculas(participantes[i][0], nombre_buscado):
            return (participantes[i][0], participantes[i][1], participantes[i][2], participantes[i][3], participantes[i][4])
    return None


def top3_participantes(participantes: list, cantidad_participantes: int) -> list:
    '''
    Obtiene los 3 participantes con mayor promedio.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de tuplas (nombre, promedio) ordenada de mayor a menor (máximo 3 elementos).
    '''
    indices = [0] * cantidad_participantes
    for i in range(cantidad_participantes):
        indices[i] = i

    # Ordenar índices por promedio
    for i in range(cantidad_participantes):
        for j in range(cantidad_participantes - i - 1):
            if participantes[indices[j]][4] < participantes[indices[j + 1]][4]:
                temp = indices[j]
                indices[j] = indices[j + 1]
                indices[j + 1] = temp

    # Crear la lista de top 3 (o menos si no hay suficientes)
    tope = 3
    if cantidad_participantes < 3:
        tope = cantidad_participantes

    resultado = [("", 0.0)] * tope
    for i in range(tope):
        nombre = participantes[indices[i]][0]
        promedio = participantes[indices[i]][4]
        resultado[i] = (nombre, promedio)

    return resultado


def participantes_ordenados(participantes: list, cantidad_participantes: int) -> list:
    '''
    Devuelve los participantes ordenados alfabéticamente por nombre.

    Args:
        participantes (list): Lista de participantes [nombre, jurado1, jurado2, jurado3, promedio].
        cantidad_participantes (int): Número de participantes.

    Returns:
        list: Lista de tuplas (nombre, jurado1, jurado2, jurado3, promedio) ordenada alfabéticamente.
    '''
    indices = [0] * cantidad_participantes
    for i in range(cantidad_participantes):
        indices[i] = i

    # Ordenar índices alfabéticamente
    for i in range(cantidad_participantes):
        for j in range(cantidad_participantes - i - 1):
            if comparar_strings_ignorando_mayusculas(participantes[indices[j]][0], participantes[indices[j + 1]][0]):
                pass
            elif participantes[indices[j]][0] > participantes[indices[j + 1]][0]:
                temp = indices[j]
                indices[j] = indices[j + 1]
                indices[j + 1] = temp

    # Crear la lista final ordenada
    resultado = [("", 0, 0, 0, 0.0)] * cantidad_participantes
    for i in range(cantidad_participantes):
        idx = indices[i]
        resultado[i] = (participantes[idx][0], participantes[idx][1], participantes[idx][2], participantes[idx][3], participantes[idx][4])

    return resultado