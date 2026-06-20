import FuncionesTPO
import MenusTPO
import DatosTPO

# Ignacio Diaz
def ejecutar_menu(datos):
    salir = False

    while salir == False:

        MenusTPO.menu_opciones()

        opcion = FuncionesTPO.colorear_input("Seleccione una opcion: ", "amarillo")

        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
            FuncionesTPO.imprimir_error("Opcion invalida. Seleccione entre 1 y 5.")
            opcion = FuncionesTPO.colorear_input("Ingrese una opcion valida: ", "rojo")

        if opcion == "1":
            FuncionesTPO.registrar_producto(datos)

        elif opcion == "2":
            FuncionesTPO.eliminar_producto(datos)

        elif opcion == "3":
            FuncionesTPO.modificar_producto(datos)

        elif opcion == "4":
            FuncionesTPO.mostrar_informe(datos)

        elif opcion == "5":
            FuncionesTPO.imprimir_informacion("Saliendo del programa...")
            salir = True

#Tomas Ruano
def main():
    datos = DatosTPO.crearDatosIniciales()
    ejecutar_menu(datos)


main()