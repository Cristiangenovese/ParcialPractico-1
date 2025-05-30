import os
import Funciones
import Inputs

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n*** MENÚ PRINCIPAL ***")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Mostrar participantes con promedio < 4")
    print("5. Mostrar participantes con promedio < 8")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Jurado más generoso")
    print("9. Participantes con puntuaciones iguales")
    print("10. Buscar participante por nombre")
    print("11. Top 3")
    print("12. Participantes ordenados alfabéticamente")
    print("0. Salir")

def main():
    cantidad_participantes = 5  # Cambiar este valor si querés más o menos participantes

    participantes_cargados = False
    puntuaciones_cargadas = False

    while True:
        limpiar_consola()
        mostrar_menu()
        opcion = Inputs.validar_opcion_menu()

        limpiar_consola()

        if opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        elif opcion == 1:
            participantes_cargados = Funciones.cargar_participantes(cantidad_participantes)

        elif opcion == 2:
            if participantes_cargados:
                puntuaciones_cargadas = Funciones.cargar_puntuaciones()
            else:
                print("Primero debe cargar los participantes.")

        elif opcion == 3:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.mostrar_puntuaciones()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 4:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.participantes_promedio_menor_4()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 5:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.participantes_promedio_menor_8()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 6:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.promedio_por_jurado()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 7:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.jurado_mas_estricto()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 8:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.jurado_mas_generoso()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 9:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.participantes_puntajes_iguales()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 10:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.buscar_participante()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 11:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.top3_participantes()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        elif opcion == 12:
            if participantes_cargados and puntuaciones_cargadas:
                Funciones.participantes_ordenados()
            else:
                print("Debe cargar los participantes y las puntuaciones primero.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()