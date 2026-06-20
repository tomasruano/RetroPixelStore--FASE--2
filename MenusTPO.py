#Ignacio Diaz
import FuncionesTPO
def menu_opciones():
    '''Muestra el menú de opciones al usuario.'''
    FuncionesTPO.imprimir_informacion("-"*50)
    FuncionesTPO.imprimir_importante("SISTEMA DE GESTIÓN: RETROPIXEL STORE")
    FuncionesTPO.imprimir_informacion("-"*50)
    FuncionesTPO.imprimir_informacion("1. Registrar producto(Alta)")
    FuncionesTPO.imprimir_informacion("2. Eliminar producto(Baja)")
    FuncionesTPO.imprimir_informacion("3. Modificar producto(Mod)")
    FuncionesTPO.imprimir_informacion("4. Informe General-Visualización de datos")
    FuncionesTPO.imprimir_informacion("5. Salir")
    FuncionesTPO.imprimir_informacion("-"*50)

#Ignacio Diaz
def menu_modificar():
    '''Muestra el menú de atributos modificables al usuario.'''
    FuncionesTPO.imprimir_informacion("-"*50)
    FuncionesTPO.imprimir_informacion("Atributos modificables:")
    FuncionesTPO.imprimir_informacion("1. Título")
    FuncionesTPO.imprimir_informacion("2. Contenido")
    FuncionesTPO.imprimir_informacion("3. Plataforma")
    FuncionesTPO.imprimir_informacion("4. Precio")
    FuncionesTPO.imprimir_informacion("5. Stock")
    FuncionesTPO.imprimir_informacion("6. Categoría")
    FuncionesTPO.imprimir_informacion("7. Disponibilidad")
    FuncionesTPO.imprimir_informacion("-"*50)

def mostrar_plataforma_maxima(plataforma, cantidad):
    '''Muestra en pantalla el resultado del informe de plataforma con mayor cantidad de productos.'''
    FuncionesTPO.imprimir_importante("-" * 50)
    
    if plataforma != "":
        FuncionesTPO.imprimir_importante("La plataforma con mayor cantidad de productos es:")
        FuncionesTPO.imprimir_importante("-" * 50)
        
        FuncionesTPO.imprimir_informacion(f"- {plataforma}: {cantidad} productos")
    else:
        FuncionesTPO.imprimir_error("No hay productos registrados en el sistema.")
        
    FuncionesTPO.imprimir_informacion("-" * 50)

def mostrar_informe_precios_promedio(resultado_informe):
    '''Muestra en pantalla el resultado del informe de precios promedio por categoría.'''
    # Separamos las dos listas que vienen adentro del resultado
    categorias = resultado_informe[0]
    promedios = resultado_informe[1]

    FuncionesTPO.imprimir_importante("-" * 50)
    
    if len(categorias) > 0:
        FuncionesTPO.imprimir_importante("PRECIO PROMEDIO POR CATEGORÍA")
        FuncionesTPO.imprimir_importante("-" * 50)
        
        for i in range(len(categorias)):
            # Mostramos cada categoría con su promedio formateado
            FuncionesTPO.imprimir_informacion(f"- {categorias[i].ljust(20)}: ${promedios[i]}")
    else:
        FuncionesTPO.imprimir_error("No hay productos registrados en el sistema.")
        
    FuncionesTPO.imprimir_informacion("-" * 50)

def mostrar_menu_categorias(categorias_disponibles):
    '''Muestra en pantalla las categorías actuales y la opción de agregar una nueva.'''
    FuncionesTPO.imprimir_informacion("\nCategorías disponibles en el sistema:")
    
    i = 0
    while i < len(categorias_disponibles):
        FuncionesTPO.imprimir_informacion(f"{i + 1} - {categorias_disponibles[i]}")
        i += 1
        
    FuncionesTPO.imprimir_importante(f"{len(categorias_disponibles) + 1} - Registrar nueva categoría")

def mostrar_informe_matricial(matriz_conteo, opciones_categoria, opciones_disponibilidad):
    '''Muestra en pantalla el informe matricial de conteo de productos por categoría y disponibilidad.'''

    FuncionesTPO.imprimir_importante("INFORME MATRICIAL")

    encabezado = "Categoría".ljust(20)

    columna = 0
    while columna < len(opciones_disponibilidad):
        encabezado += opciones_disponibilidad[columna].ljust(15)
        columna += 1

    FuncionesTPO.imprimir_importante(encabezado)

    fila = 0
    while fila < len(opciones_categoria):

        linea = opciones_categoria[fila].ljust(20)

        columna = 0
        while columna < len(opciones_disponibilidad):
            linea += str(matriz_conteo[fila][columna]).ljust(15)
            columna += 1

        FuncionesTPO.imprimir_informacion(linea)
        fila += 1