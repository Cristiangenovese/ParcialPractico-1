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
    cantidad_participantes = 3
    participantes = [["", 0, 0, 0, 0.0] for _ in range(cantidad_participantes)]

    participantes_cargados = False
    puntuaciones_cargadas = False

    while True:
        limpiar_consola()
        mostrar_menu()

        opcion_str = input("Ingrese una opción del menú: ")
        opcion = Inputs.validar_opcion_menu(opcion_str)
        if opcion is None:
            print("Opción inválida. Debe ser un número entre 0 y 12.")
            input("\nPresione Enter para continuar...")
            continue

        limpiar_consola()

        if opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        elif opcion == 1:
            for i in range(cantidad_participantes):
                while True:
                    nombre_ingresado = input(f"Ingrese el nombre del participante {i+1}: ")
                    nombre_validado = Inputs.validar_nombre(nombre_ingresado)
                    if nombre_validado is not None:
                        participantes[i][0] = nombre_validado
                        participantes[i][1] = 0
                        participantes[i][2] = 0
                        participantes[i][3] = 0
                        participantes[i][4] = 0.0
                        break
                    else:
                        print("Nombre inválido. Debe tener al menos 3 letras y solo caracteres alfabéticos o espacios.")
            participantes_cargados = True
            print("Participantes cargados correctamente.")

        elif opcion == 2:
            if participantes_cargados:
                for i in range(cantidad_participantes):
                    print(f"\nCargando puntajes para {participantes[i][0]}:")
                    for j in range(1, 4):
                        while True:
                            puntaje_ingresado = input(f"Ingrese la puntuación del jurado {j} (1 a 10): ")
                            puntaje_validado = Inputs.validar_puntaje(puntaje_ingresado)
                            if puntaje_validado is not None:
                                participantes[i][j] = puntaje_validado
                                break
                            else:
                                print("Puntaje inválido. Debe ser un número entre 1 y 10.")
                    participantes[i][4] = (participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3
                puntuaciones_cargadas = True
                print("Puntuaciones cargadas correctamente.")
            else:
                print("Primero debe cargar los participantes (opción 1).")

        else:
            if not participantes_cargados:
                print("Primero debe cargar los participantes (opción 1).")
            elif not puntuaciones_cargadas:
                print("Primero debe cargar las puntuaciones (opción 2).")
            else:
                if opcion == 3:
                    datos = Funciones.mostrar_puntuaciones(participantes, cantidad_participantes)
                    for nombre, p1, p2, p3, promedio in datos:
                        print(f"{nombre} | Puntajes: [{p1}, {p2}, {p3}] | Promedio: {promedio:.2f}")

                elif opcion == 4:
                    resultados = Funciones.participantes_promedio_menor_4(participantes, cantidad_participantes)
                    if resultados:
                        for nombre, promedio in resultados:
                            print(f"{nombre} - Promedio: {promedio:.2f}")
                    else:
                        print("No hay participantes con promedio menor a 4.")

                elif opcion == 5:
                    resultados = Funciones.participantes_promedio_menor_8(participantes, cantidad_participantes)
                    if resultados:
                        for nombre, promedio in resultados:
                            print(f"{nombre} - Promedio: {promedio:.2f}")
                    else:
                        print("No hay participantes con promedio menor a 8.")

                elif opcion == 6:
                    promedios_jurados = Funciones.promedio_por_jurado(participantes, cantidad_participantes)
                    for i, promedio in enumerate(promedios_jurados):
                        print(f"Jurado {i+1}: {promedio:.2f}")

                elif opcion == 7:
                    jurados = Funciones.jurado_mas_estricto(participantes, cantidad_participantes)
                    print("Jurado(s) más estricto(s):", end=" ")
                    for i in range(len(jurados)):
                        print(f"Jurado {jurados[i]}", end="")
                        if i < len(jurados) - 1:
                            print(", ", end="")
                    print()

                elif opcion == 8:
                    jurados = Funciones.jurado_mas_generoso(participantes, cantidad_participantes)
                    print("Jurado(s) más generoso(s):", end=" ")
                    for i in range(len(jurados)):
                        print(f"Jurado {jurados[i]}", end="")
                        if i < len(jurados) - 1:
                            print(", ", end="")
                    print()

                elif opcion == 9:
                    resultados = Funciones.participantes_puntajes_iguales(participantes, cantidad_participantes)
                    if resultados:
                        for nombre in resultados:
                            print(f"{nombre} tiene los mismos puntajes en los 3 jurados.")
                    else:
                        print("No hay participantes con puntajes iguales en los 3 jurados.")

                elif opcion == 10:
                    nombre_buscado = input("Ingrese el nombre del participante a buscar: ")
                    nombre_validado = Inputs.validar_nombre(nombre_buscado)
                    if nombre_validado is not None:
                        resultado = Funciones.buscar_participante(participantes, cantidad_participantes, nombre_validado)
                        if resultado:
                            nombre, p1, p2, p3, promedio = resultado
                            print(f"Nombre: {nombre} | Puntajes: [{p1}, {p2}, {p3}] | Promedio: {promedio:.2f}")
                        else:
                            print("Participante no encontrado.")
                    else:
                        print("Nombre inválido.")

                elif opcion == 11:
                    top3 = Funciones.top3_participantes(participantes, cantidad_participantes)
                    if top3:
                        for nombre, promedio in top3:
                            print(f"{nombre} - Promedio: {promedio:.2f}")
                    else:
                        print("No hay datos para mostrar.")

                elif opcion == 12:
                    ordenados = Funciones.participantes_ordenados(participantes, cantidad_participantes)
                    for nombre, p1, p2, p3, promedio in ordenados:
                        print(f"{nombre} | Puntajes: [{p1}, {p2}, {p3}] | Promedio: {promedio:.2f}")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
