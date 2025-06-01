def validar_opcion_menu(opcion_str: str) -> int or None:
    '''
    Valida una opción del menú (debe ser un número entre 0 y 12).

    Args:
        opcion_str (str): Opción ingresada como string.

    Returns:
        int: Opción válida (entre 0 y 12), o None si es inválido.
    '''
    if opcion_str and all('0' <= c <= '9' for c in opcion_str):
        opcion_int = int(opcion_str)
        if 0 <= opcion_int <= 12:
            return opcion_int
    return None

def limpiar_espacios(texto: str) -> str:
    '''
    Elimina los espacios al inicio y al final de una cadena.

    Args:
        texto (str): Texto a limpiar.

    Returns:
        str: Texto limpio.
    '''
    inicio = 0
    fin = len(texto) - 1

    while inicio <= fin and texto[inicio] == ' ':
        inicio += 1

    while fin >= inicio and texto[fin] == ' ':
        fin -= 1

    return texto[inicio:fin+1]


def formatear_titulo(texto: str) -> str:
    '''
    Convierte la primera letra de cada palabra en mayúscula y el resto en minúscula, usando ASCII.

    Args:
        texto (str): Texto a formatear.

    Returns:
        str: Texto formateado.
    '''
    resultado = ""
    nueva_palabra = True

    for caracter in texto:
        if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
            if nueva_palabra:
                if 'a' <= caracter <= 'z':
                    resultado += chr(ord(caracter) - 32)
                else:
                    resultado += caracter
                nueva_palabra = False
            else:
                if 'A' <= caracter <= 'Z':
                    resultado += chr(ord(caracter) + 32)
                else:
                    resultado += caracter
        else:
            resultado += caracter
            if caracter == ' ':
                nueva_palabra = True

    return resultado


def validar_nombre(nombre: str) -> str or None:
    '''
    Valida un nombre (al menos 3 letras, solo letras y espacios).

    Args:
        nombre (str): Nombre a validar.

    Returns:
        str: Nombre formateado si es válido, None si no.
    '''
    nombre = limpiar_espacios(nombre)

    if len(nombre) >= 3 and all(('A' <= c <= 'Z') or ('a' <= c <= 'z') or (c == ' ') for c in nombre):
        return formatear_titulo(nombre)
    return None


def validar_puntaje(puntaje_str: str) -> int or None:
    '''
    Valida un puntaje (debe ser número entre 1 y 10).

    Args:
        puntaje_str (str): Puntaje ingresado como string.

    Returns:
        int: Puntaje válido (1 a 10) o None si es inválido.
    '''
    if puntaje_str and all('0' <= c <= '9' for c in puntaje_str):
        puntaje_int = int(puntaje_str)
        if 1 <= puntaje_int <= 10:
            return puntaje_int
    return None