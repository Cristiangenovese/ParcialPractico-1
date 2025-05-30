def validar_opcion_menu():
    """
    Valida la opción ingresada por el usuario para el menú principal.

    Devuelve:
    - (int) Opción seleccionada (número entre 0 y 12).
    """
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion and all('0' <= c <= '9' for c in opcion):
            opcion_int = int(opcion)
            if 0 <= opcion_int <= 12:
                return opcion_int
            else:
                print("La opción debe estar entre 0 y 12.")
        else:
            print("Debe ingresar un número válido.")


def limpiar_espacios(texto: str) -> str:
    '''
    Elimina los espacios al inicio y al final de una cadena de texto.

    Args:
        texto (str): Texto a limpiar.

    Returns:
        str: Texto sin espacios al inicio ni al final.
    '''
    inicio = 0
    fin = len(texto) - 1

    # Buscar el primer carácter que no sea espacio desde el inicio
    while inicio <= fin and texto[inicio] == ' ':
        inicio += 1

    # Buscar el último carácter que no sea espacio desde el final
    while fin >= inicio and texto[fin] == ' ':
        fin -= 1

    # Extraer el texto limpio
    return texto[inicio:fin+1]


def formatear_titulo(texto: str) -> str:
    '''
    Convierte la primera letra de cada palabra en mayúscula y el resto en minúscula, usando ASCII.
    '''
    resultado = ""
    nueva_palabra = True

    for caracter in texto:
        if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
            if nueva_palabra:
                # Convertir a mayúscula
                if 'a' <= caracter <= 'z':
                    resultado += chr(ord(caracter) - 32)
                else:
                    resultado += caracter
                nueva_palabra = False
            else:
                # Convertir a minúscula
                if 'A' <= caracter <= 'Z':
                    resultado += chr(ord(caracter) + 32)
                else:
                    resultado += caracter
        else:
            resultado += caracter
            if caracter == ' ':
                nueva_palabra = True

    return resultado


def validar_nombre() -> str:
    '''
    Solicita y valida el nombre de un participante.

    El nombre debe tener al menos 3 caracteres y solo contener letras (A-Z, a-z) y espacios.

    Returns:
        str: Nombre validado, con la primera letra de cada palabra en mayúscula.
    '''
    while True:
        nombre = limpiar_espacios(input("Ingrese el nombre del participante: "))

        # Verifica que tenga al menos 3 caracteres y solo letras o espacios
        if len(nombre) >= 3 and all(('A' <= c <= 'Z') or ('a' <= c <= 'z') or (c == ' ') for c in nombre):
            return formatear_titulo(nombre)
        else:
            print("El nombre debe tener al menos 3 caracteres y solo letras y espacios.")


def validar_puntaje(jurado_num):
    """
    Valida el puntaje ingresado para un jurado.

    Parámetros:
    - jurado_num (int): Número del jurado (1, 2 o 3) para mostrar en el mensaje.

    Devuelve:
    - (int) Puntaje ingresado (entre 1 y 10).
    """
    while True:
        puntaje = input(f"Ingrese la puntuación del jurado {jurado_num} (1 a 10): ")
        if puntaje and all('0' <= c <= '9' for c in puntaje):
            puntaje_int = int(puntaje)
            if 1 <= puntaje_int <= 10:
                return puntaje_int
            else:
                print("El puntaje debe estar entre 1 y 10.")
        else:
            print("Debe ingresar un número válido.")


def confirmar_busqueda() -> str:
    '''
    Solicita el nombre de un participante para realizar una búsqueda.

    Returns:
        str: Nombre formateado con la primera letra de cada palabra en mayúscula.
    '''
    nombre = limpiar_espacios(input("Ingrese el nombre del participante: "))
    return formatear_titulo(nombre)