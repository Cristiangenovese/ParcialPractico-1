def validar_opcion_menu() -> int:
    '''
    Solicita al usuario una opción del menú, la valida y la devuelve como número entero.

    La opción debe ser un número entero entre 0 y 12 inclusive.

    Returns:
        int: Opción seleccionada por el usuario (0 a 12).
    '''
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion <= 12:
                return opcion
            else:
                print("La opción debe estar entre 0 y 12.")
        else:
            print("Debe ingresar un número.")


def validar_nombre() -> str:
    '''
    Solicita y valida el nombre de un participante.

    El nombre debe tener al menos 3 caracteres y solo contener letras y espacios.

    Returns:
        str: Nombre validado, con la primera letra de cada palabra en mayúscula.
    '''
    while True:
        nombre = input("Ingrese el nombre del participante: ").strip()
        if len(nombre) >= 3 and all(c.isalpha() or c.isspace() for c in nombre):
            return nombre.title()
        else:
            print("El nombre debe tener al menos 3 caracteres y solo letras y espacios.")


def validar_puntaje(jurado_num: int) -> int:
    '''
    Solicita y valida la puntuación de un jurado para un participante.

    Args:
        jurado_num (int): Número del jurado (1, 2 o 3) para mostrar en el mensaje.

    Returns:
        int: Puntaje válido entre 1 y 10.
    '''
    while True:
        puntaje = input(f"Ingrese la puntuación del jurado {jurado_num} (1 a 10): ")
        if puntaje.isdigit():
            puntaje = int(puntaje)
            if 1 <= puntaje <= 10:
                return puntaje
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
    nombre = input("Ingrese el nombre del participante a buscar: ").strip()
    return nombre.title()
