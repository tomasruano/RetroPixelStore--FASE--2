import DatosTPO
import MenusTPO
import random
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

# =========================================================================
#                                   INDICE
# =========================================================================
# Lineas 19  a 318  ->  BLOQUE 1: ALTA DE PRODUCTOS (Carga)
# Lineas 320 a 414  ->  BLOQUE 2: BAJA DE PRODUCTOS (Eliminar)
# Lineas 416 a 520  ->  BLOQUE 3: MODIFICACIÓN (Edición)
# Lineas 522 a 745  ->  BLOQUE 4: REPORTES Y CÁLCULOS (Informes)
# Lineas 747 a 858  ->  BLOQUE 5: HERRAMIENTAS Y VALIDACIONES
# =========================================================================

# =========================================================================
# OPERACIÓN: ALTA DE PRODUCTOS (Carga)
# =========================================================================
# Funciones relacionadas con el ingreso y validación de nuevos productos.

#Ignacio Diaz
def carga():
    imprimir_informacion("1. Carga manual")
    imprimir_informacion("2. Carga aleatoria")

    opcion = colorear_input("Seleccione una opción: ", "amarillo")

    while opcion != "1" and opcion != "2":
        opcion = colorear_input("Error. Ingrese 1 o 2: ", "rojo")

    return opcion
#Ignacio Diaz
def cantidad_titulos_a_registrar(datos):
    cantidad = ingresar_entero_no_negativo("Ingrese la cantidad de productos a registrar: ")

    while cantidad <= 0:
        cantidad = ingresar_entero_no_negativo("Error. Ingrese una cantidad mayor a 0: ")

    return cantidad
#Tomas Ruano
def pedir_titulo(datos):
    titulo = colorear_input("Ingrese el titulo: ", "amarillo")

    while titulo == "" or producto_duplicado(datos, titulo):

        if titulo == "":
            imprimir_error("El titulo no puede estar vacio.")
        else:
            imprimir_informacion("Ese producto ya existe.")

        titulo = colorear_input("Ingrese otro titulo: ", "amarillo")

    return titulo
#Tomas Ruano
def existe_categoria_duplicada(lista_categorias, categoria_buscada):
    '''Determina secuencialmente si una categoría ya existe en la lista de categorías disponibles, ignorando mayúsculas y minúsculas.'''
    duplicado = False
    i = 0
    while i < len(lista_categorias):
        if lista_categorias[i].lower() == categoria_buscada.lower():
            duplicado = True
        i += 1
    return duplicado
#Ignacio Diaz
def existe_en_producto(lista_producto, categoria_buscada):
    '''Determina si el producto actual ya tiene asignada esa categoría para evitar repetidos de forma local en el proceso de selección de categoría.'''
    ya_asignada = False
    i = 0
    while i < len(lista_producto):
        if lista_producto[i] == categoria_buscada:
            ya_asignada = True
        i += 1
    return ya_asignada
#Gaspar Divano
def seleccionar_categoria(datos):
    '''Permite seleccionar una categoría existente o crear una nueva.'''
    categorias_disponibles = datos[9]
    categoria_seleccionada = ""

    MenusTPO.mostrar_menu_categorias(categorias_disponibles)

    # La última opción del menú corresponde a agregar una nueva categoría
    limite_opciones = len(categorias_disponibles) + 1
    entrada = colorear_input("\nSeleccione una opción numérica: ", "amarillo")
    
    # Validamos que sea un número entero
    while entrada == "" or entrada.isdigit() == False:
        imprimir_error("Debe ingresar un valor numérico entero.")
        entrada = colorear_input("Ingrese una opción válida: ", "rojo")
        
    opcion = int(entrada)
    
    # Validamos que el número esté dentro del rango del menú
    while opcion < 1 or opcion > limite_opciones:
        imprimir_error(f"Opción inválida. Debe ser un número entre 1 y {limite_opciones}.")
        entrada = colorear_input("Ingrese una opción válida: ", "rojo")
        while entrada == "" or not entrada.isdigit():
            imprimir_error("Debe ingresar un valor numérico entero.")
            entrada = colorear_input("Ingrese una opción válida: ", "rojo")
        opcion = int(entrada)

    if opcion == limite_opciones:
        # El usuario quiere registrar una nueva categoría
        nueva_cat = colorear_input("Ingrese el nombre de la nueva categoría: ", "amarillo")
        
        es_valida = False
        while es_valida == False:
            if nueva_cat == "":
                imprimir_error("La categoría no puede estar vacía.")
                nueva_cat = colorear_input("Ingrese un nombre válido: ", "rojo")
            elif existe_categoria_duplicada(categorias_disponibles, nueva_cat) == True:
                imprimir_error(f"La categoría '{nueva_cat}' ya existe en el sistema.")
                nueva_cat = colorear_input("Ingrese una categoría diferente: ", "rojo")
            else:
                es_valida = True
            
        categorias_disponibles.append(nueva_cat)
        categoria_seleccionada = nueva_cat
    else:
        categoria_seleccionada = categorias_disponibles[opcion - 1]

    return categoria_seleccionada
#Gaspar Divano
def seleccionar_multiples_categorias(datos):
    '''Permite asociar una o más categorías a un producto.'''

    categorias_del_producto = []
    continuar = "si"

    while continuar.lower() == "si" or len(categorias_del_producto) == 0:

        cat_elegida = seleccionar_categoria(datos)

        if existe_en_producto(categorias_del_producto, cat_elegida):
            imprimir_error(f"El producto ya tiene asignada la categoría '{cat_elegida}'.")
        else:
            categorias_del_producto.append(cat_elegida)
            imprimir_importante(f"Categoría '{cat_elegida}' asociada.")

        entrada_seguir = colorear_input(
            "¿Desea asociar otra categoría a este producto? (si/no): ",
            "amarillo"
        )

        while entrada_seguir.lower() != "si" and entrada_seguir.lower() != "no":
            imprimir_error("Opción inválida. Ingrese 'si' o 'no'.")
            entrada_seguir = colorear_input(
                "¿Desea asociar otra categoría? (si/no): ",
                "rojo"
            )

        continuar = entrada_seguir

        if continuar.lower() == "no" and len(categorias_del_producto) == 0:
            imprimir_error("Un producto no puede registrarse sin al menos una categoría asociada.")
            continuar = "si" # Lo forzamos a seguir hasta que cargue una válida

    return categorias_del_producto
#Tomas Sobrino
def guardar_producto(datos, titulo_nuevo, contenido_nuevo, plataforma_nueva,
                     precio_nuevo, stock_nuevo, categoria_nueva, disponibilidad_nueva):

    datos[0].append(titulo_nuevo)
    datos[1].append(contenido_nuevo)
    datos[2].append(plataforma_nueva)
    datos[3].append(precio_nuevo)
    datos[4].append(stock_nuevo)
    datos[5].append(categoria_nueva)
    datos[6].append(disponibilidad_nueva)
#Tomas Ruano
def registrar_producto_manual(datos):
    
    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    cantidad = cantidad_titulos_a_registrar(datos)
    for i in range(cantidad):
        imprimir_importante("-" * 50)
        imprimir_importante(f"Producto {i + 1}")
        imprimir_importante("-" * 50)
        nuevo_titulo = pedir_titulo(datos)

        nuevo_contenido = ingresar_opcion_valida(
            "Ingrese el contenido: ",
            opciones_contenido
        )

        nueva_plataforma = ingresar_opcion_valida(
            "Ingrese la plataforma: ",
            opciones_plataforma
        )

        nuevo_precio = ingresar_float_positivo(
            "Ingrese el precio: "
        )

        nuevo_stock = ingresar_entero_no_negativo(
            "Ingrese el stock: "
        )

        lista_categorias_producto = seleccionar_multiples_categorias(datos)

        nueva_disponibilidad = ingresar_opcion_valida(
            "Ingrese la disponibilidad: ",
            opciones_disponibilidad
        )

        guardar_producto(
            datos,
            nuevo_titulo,
            nuevo_contenido,
            nueva_plataforma,
            nuevo_precio,
            nuevo_stock,
            lista_categorias_producto,
            nueva_disponibilidad
        )
        imprimir_importante("Producto agregado correctamente")
# Tomas Ruano
def es_plataforma_de_pelicula(plataforma):
    '''Determina mediante comparación directa si una plataforma pertenece al formato de películas.'''
    aux = plataforma.lower()
    
    # Comprobamos estrictamente con operaciones lógicas puras
    if aux == "dvd" or aux == "blue ray" or aux == "blu-ray":
        resultado = True
    else:
        resultado = False
        
    return resultado        
#Tomas Ruano
def registrar_producto_aleatorio(datos):

    opciones_plataforma = datos[8]
    opciones_disponibilidad = datos[10]

    random_data = DatosTPO.obtener_titulos_y_categorias()

    titulos = random_data[0]
    categorias = random_data[1]

    titulos_disponibles = 0

    for i in range(len(titulos)):
        if not producto_duplicado(datos, titulos[i]):
            titulos_disponibles += 1

    if titulos_disponibles == 0:
        imprimir_error("No hay más títulos disponibles para generar aleatoriamente.")    
    else:
        indice = generar_indice_aleatorio_lista(titulos)
        nuevo_titulo = titulos[indice]

        while producto_duplicado(datos, nuevo_titulo):
            indice = generar_indice_aleatorio_lista(titulos)
            nuevo_titulo = titulos[indice]

        nueva_categoria = categorias[indice]

        if indice <= 3:
            nuevo_contenido = "Videojuego"
        else:
            nuevo_contenido = "Pelicula"

        indice_plataforma = generar_indice_aleatorio_lista(opciones_plataforma)
        nueva_plataforma = opciones_plataforma[indice_plataforma]

        # Validamos que la plataforma sea coherente con el contenido generado, y si no lo es, generamos una nueva plataforma hasta que sea compatible. Por ejemplo, si el contenido es película, la plataforma debe ser Blu-Ray o DVD, y si el contenido es videojuego, la plataforma debe ser Playstation 5, Xbox Series X o PC.
        while (nuevo_contenido == "Pelicula" and es_plataforma_de_pelicula(nueva_plataforma) == False) or (nuevo_contenido == "Videojuego" and es_plataforma_de_pelicula(nueva_plataforma) == True):
    
            indice_plataforma = generar_indice_aleatorio_lista(opciones_plataforma)
            nueva_plataforma = opciones_plataforma[indice_plataforma]

        nuevo_precio = float(random.randint(1000, 100000))

        nuevo_stock = random.randint(0, 50)

        indice_disponibilidad = generar_indice_aleatorio_lista(opciones_disponibilidad)
        nueva_disponibilidad = opciones_disponibilidad[indice_disponibilidad]

        guardar_producto(
            datos,
            nuevo_titulo,
            nuevo_contenido,
            nueva_plataforma,
            nuevo_precio,
            nuevo_stock,
            nueva_categoria,
            nueva_disponibilidad
        )
        imprimir_importante(f"Producto: {nuevo_titulo} agregado correctamente")
#Tomas Ruano
def registrar_producto(datos):

    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    opcion = carga()

    if opcion == "1":
        registrar_producto_manual(datos)

    else:

        registrar_producto_aleatorio(datos)

# =========================================================================
# OPERACIÓN: BAJA DE PRODUCTOS (Eliminación)
# =========================================================================
# Funciones encargadas de remover productos del sistema de forma segura.

#Agustin Fani
def verificar_eliminables(stock, disponibilidad, titulo):
    imprimir_importante("Productos eliminables:")
    i = 0
    lista_eliminables = []
    while i < len(stock):
        if stock[i] == 0 and disponibilidad[i].lower() == "discontinuado":
            lista_eliminables.append(titulo[i])
        i += 1
    if len(lista_eliminables) == 0:
        imprimir_informacion("No hay productos eliminables.")
        continuar=False
    else:
        for producto in lista_eliminables:
            imprimir_importante(f"- {producto}")#ponemos el mensaje asi porque sino cuando concatenamos con , lo toma como muchos parametros cuando la funcion recibe uno solo
            continuar=True
    return continuar
#Agustin Fani
def es_eliminable(stock, disponibilidad, indice):
    eliminable = False

    if stock[indice] == 0 and disponibilidad[indice].lower() == "discontinuado":
        eliminable = True

    return eliminable
#Agustin Fani
def eliminar_por_indice(datos, indice):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    titulo.pop(indice)
    contenido.pop(indice)
    plataforma.pop(indice)
    precio.pop(indice)
    stock.pop(indice)
    categoria.pop(indice)
    disponibilidad.pop(indice)
#Agustin Fani
def eliminar_producto(datos):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    continuar = True
    indice = -1

    continuar = verificar_eliminables(stock, disponibilidad, titulo)
    
    while continuar == True and indice == -1:
        titulo_buscado = colorear_input("Ingrese el titulo a eliminar o 'volver': ","amarillo")

        if titulo_buscado.lower() == "volver":
            imprimir_informacion("Volviendo al menu principal...")
            continuar = False
        else:
            indice = buscar_indice(titulo, titulo_buscado)

            if indice == -1:
                imprimir_informacion("No se encontro el producto.")

    if continuar == True:

        if es_eliminable(stock, disponibilidad, indice):

            confirmacion = colorear_input("Confirma eliminar? (si/no): ", "amarillo")

            while confirmacion.lower() != "si" and confirmacion.lower() != "no":
                imprimir_error("Opcion no valida. Ingrese 'si' para confirmar o 'no' para cancelar.")
                confirmacion = colorear_input("Confirma eliminar? (si/no): ", "amarillo")

            if confirmacion.lower() == "si":
                eliminar_por_indice(datos, indice)
                imprimir_importante("Producto eliminado correctamente.")
            else:
                imprimir_informacion("Eliminacion cancelada.")

        else:
            imprimir_informacion("No se puede eliminar el producto. ")
            imprimir_informacion("El stock debe ser 0 y la disponibilidad debe ser 'Discontinuado'.")

# =========================================================================
# OPERACIÓN: MODIFICACIÓN DE PRODUCTOS (Edición)
# =========================================================================
# Funciones para editar stock, precios o datos de productos existentes.

#Tomas Sobrino
def aplicar_cambio_atributo(opcion, indice, datos):
    '''Modifica un atributo en el índice seleccionado de las listas paralelas'''
 #asignamos cada lista a una variable para facilitar la lectura del código
    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]
 #listas de opciones para validar que lo que escriban sea correcto
    opciones_contenido = datos[7]
    opciones_plataforma = datos[8]
    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    if opcion == "1":
        nuevo_titulo = colorear_input("Ingrese el nuevo título: ", "amarillo")
        while nuevo_titulo == "":
            nuevo_titulo = colorear_input("El título no puede estar vacío. Ingrese nuevo título: ", "rojo")
        titulo[indice] = nuevo_titulo
    elif opcion == "2":
        contenido[indice] = ingresar_opcion_valida("Ingrese el nuevo contenido: ", opciones_contenido)
    elif opcion == "3":
        plataforma[indice] = ingresar_opcion_valida("Ingrese la nueva plataforma: ", opciones_plataforma)
    elif opcion == "4":
        precio[indice] = ingresar_float_positivo("Ingrese el nuevo precio: ")
    elif opcion == "5":
        stock[indice] = ingresar_entero_no_negativo("Ingrese el nuevo stock: ")
    elif opcion == "6":
        imprimir_importante(f"Modificando categorías para: {titulo[indice]}")
        categoria[indice] = seleccionar_multiples_categorias(datos)
    elif opcion == "7":
        disponibilidad[indice] = ingresar_opcion_valida("Ingrese la nueva disponibilidad: ", opciones_disponibilidad)

    imprimir_importante("Producto modificado con éxito.")
#Tomas Sobrino
def modificar_producto(datos):
    '''Modifica un atributo controlando el flujo por banderas lógicas para cada paso.'''
    imprimir_importante("-" * 50)
    imprimir_importante("Modificar Producto")
    imprimir_importante("-" * 50)

    titulos = datos[0]
    #se usa continuar como bandera lógica
    continuar = True

    #verificamos que haya productos registrados
    if len(titulos) == 0:
        imprimir_informacion("No hay productos registrados para modificar.")
        continuar = False

    #hace busqueda del título a modificar, si no lo encuentra vuelve a pedirlo, se puede salir escribiendo "volver"
    if continuar:
        # primero muestra los títulos registrados para que el usuario sepa qué escribir, si no hay productos registrados muestra un mensaje y vuelve al menú principal
        imprimir_importante("Títulos registrados actualmente:")
        i = 0
        while i < len(titulos):
            imprimir_informacion(f"-  {titulos[i]}")
            i += 1
        imprimir_importante("-" * 50)

        # luego busca el índice del título ingresado en la lista de títulos, si no lo encuentra muestra un mensaje de error y vuelve a pedir el título, se puede salir escribiendo "volver"
        indice_elegido = -1
        titulo_valido = False
        
        while titulo_valido == False and continuar == True:
            titulo_buscado = colorear_input("Ingrese el título del producto a modificar o 'volver': ", "amarillo")
            
            if titulo_buscado.lower() == "volver":
                imprimir_informacion("Volviendo al menú principal...")
                continuar = False
            else:
                # busca el índice del título ingresado en la lista de títulos, si no lo encuentra muestra un mensaje de error y vuelve a pedir el título
                indice_elegido = buscar_indice(titulos, titulo_buscado)
                
                if indice_elegido != -1:
                    titulo_valido = True
                else:
                    imprimir_error("El título no se encuentra registrado. Intente nuevamente.")
    
    # si el título se encuentra, muestra el menú de atributos modificables y pide seleccionar uno, si la opción no es válida vuelve a pedirla, se puede salir escribiendo "volver"
    if continuar:
        MenusTPO.menu_modificar()
        opcion_valida = False

        while opcion_valida == False and continuar == True:
            opcion = colorear_input("Seleccione el número del atributo a modificar o 'volver': ", "amarillo")
            if opcion.lower() == "volver":
                imprimir_informacion("Volviendo al menú principal...")
                continuar = False
            else:
                if existe_en_lista(["1", "2", "3", "4", "5", "6", "7"], opcion):
                    opcion_valida = True
                else:
                    imprimir_error("Opción no válida. Debe ser entre 1 y 7.")
        #por ultimo, si se seleccionó una opción válida, se aplica el cambio en el atributo seleccionado del producto elegido usando la función aplicar_cambio_atributo
        if continuar:
            aplicar_cambio_atributo(opcion, indice_elegido, datos)

# =========================================================================
# REPORTES: CÁLCULOS E INFORMES ESTADÍSTICOS
# =========================================================================
# Funciones estadísticas: informe_general, calcular_informe_matricial, etc.

#Gaspar Divano  
def ordenamiento_burbuja(matriz):
       # Ordenamiento burbuja por stock y alfabéticamente por título en caso de empate
    for i in range(len(matriz) - 1):
        for j in range(len(matriz) - 1 - i):
            stock_actual    = matriz[j][4]
            stock_siguiente = matriz[j + 1][4]
            titulo_actual   = matriz[j][0]
            titulo_siguiente = matriz[j + 1][0]
            if (stock_actual < stock_siguiente) or (stock_actual == stock_siguiente and titulo_actual > titulo_siguiente):
            #Ordena el stock por orden descendente o en orden ascendente alfabeticamente
                aux          = matriz[j]
                matriz[j]     = matriz[j + 1]
                matriz[j + 1] = aux
#Gaspar Divano
def crear_matriz( titulo, contenido, plataforma, precio, stock, categoria, disponibilidad):
    '''crea una matriz a partir de las listas paralelas con los datos de los productos registrados. Cada fila de la matriz representa un producto y cada columna representa un atributo del producto.'''
    matriz = []
    for i in range(len(titulo)):
        fila = [
            titulo[i],
            contenido[i],
            plataforma[i],
            precio[i],
            stock[i],
            categoria[i],
            disponibilidad[i]
        ]
        matriz.append(fila)
    return matriz
#Gaspar Divano
def convertir_categorias_a_texto(categoria_producto):
    '''Dado que ahora la categoría de cada producto es una lista de categorías (asociación múltiple), esta función convierte esa lista en un texto formateado para mostrarlo en el informe general. Si la categoría viene como texto plano, se conserva igual.'''
    categoria_texto = ""
    
    # Recorremos de manera secuencial la sublista de categorías de este producto
    i = 0
    while i < len(categoria_producto):
        if i == 0:
            categoria_texto = categoria_producto[i]
        else:
            categoria_texto = categoria_texto + ", " + categoria_producto[i]
        i += 1
        
    return categoria_texto
 
#Gaspar Divano   
def informe_general(matriz):
    '''Muestra todos los productos registrados ordenados de mayor a menor
    según el stock disponible. En caso de igualdad, ordena alfabéticamente
    por título.'''
    imprimir_importante("-" * 50)
    imprimir_importante("Informe General")
    imprimir_importante("-" * 50)
    ordenamiento_burbuja(matriz)
    imprimir_importante("-" * 150)
    imprimir_importante(
        "Titulo".ljust(40) + "|" +
        "Contenido".ljust(15) + "|" +
        "Plataforma".ljust(20) + "|" +
        "Precio".ljust(12) + "|" +
        "Stock".ljust(8) + "|" +
        "Categorias".ljust(30) + "|" +
        "Disponibilidad"
    )
    imprimir_importante("-" * 150)
    for fila in matriz:
        categoria_texto = convertir_categorias_a_texto(fila[5])
        imprimir_informacion(
            str(fila[0]).ljust(40) + "|" +
            str(fila[1]).ljust(15) + "|" +
            str(fila[2]).ljust(20) + "|" +
            str(fila[3]).ljust(12) + "|" +
            str(fila[4]).ljust(8) + "|" +
            categoria_texto.ljust(30) + "|" +
            str(fila[6])
        )

    imprimir_informacion("-" * 150)
#Gaspar Divano
def calcular_plataforma_con_mas_productos(datos):
    '''Determina la plataforma con mayor cantidad de productos'''
    plataformas_productos = datos[2]
    opciones_plataforma = datos[8]

    max_cantidad = -1
    plataforma_max = ""

    # Recorremos secuencialmente las opciones válidas con un while
    i = 0
    while i < len(opciones_plataforma):
        plataforma_actual = opciones_plataforma[i]
        contador = 0

        # Recorremos los productos registrados para contar las coincidencias
        j = 0
        while j < len(plataformas_productos):
            if plataformas_productos[j].lower() == plataforma_actual.lower():
                contador += 1
            j += 1

        # Evaluamos si encontramos un nuevo máximo
        if contador > max_cantidad:
            max_cantidad = contador
            plataforma_max = plataforma_actual
            
        i += 1

    return plataforma_max, max_cantidad

def calcular_informe_matricial(datos):
    '''Calcula la cantidad de productos por categoría y disponibilidad.'''
    #asignamos cada lista a una variable para facilitar la lectura del código
    categorias = datos[5]
    disponibilidades = datos[6]

    opciones_categoria = datos[9]
    opciones_disponibilidad = datos[10]

    matriz = [] #inicializamos la matriz con ceros, con tantas filas como categorías y tantas columnas como disponibilidades

    f = 0 #fila
    while f < len(opciones_categoria):

        fila = []

        c = 0 #columna
        while c < len(opciones_disponibilidad):
            fila.append(0)
            c += 1

        matriz.append(fila)
        f += 1

    producto = 0
    while producto < len(categorias):

        disponibilidad = disponibilidades[producto]

        i = 0 #contador de categorías del producto
        while i < len(categorias[producto]):

            categoria = categorias[producto][i]

            fila = buscar_indice(opciones_categoria, categoria)
            columna = buscar_indice(opciones_disponibilidad, disponibilidad)

            if fila != -1 and columna != -1:
                matriz[fila][columna] += 1

            i += 1

        producto += 1

    return matriz
#Tomas Sobrino
def calcular_precios_promedio(datos):
    precio = datos[3]
    categoria = datos[5]

    categorias_unicas = []
    sumas_precios = []

    for i in range(len(categoria)):
        # Se agrega [0] porque categoria[i] ahora es una lista de categorías y queremos evaluar la categoría principal para el informe de precios promedio por categoría.
        # Buscamos el indice de la categoría principal en la lista de categorías únicas
        indice = buscar_indice(categorias_unicas, categoria[i][0])
        # si el indice es -1 se agrega la categoria a la lista de categorias unicas y se agrega a su vez el precio a la lista de sumas de precios
        if indice == -1:
            categorias_unicas.append(categoria[i][0])
            sumas_precios.append(precio[i])
        else:
            # si el indice es distinto de -1 se suma el precio al precio acumulado de la categoria correspondiente
            sumas_precios[indice] += precio[i]
    
    promedios_finales = []
    for i in range(len(categorias_unicas)):
        contador = 0
        for j in range(len(categoria)):
            # Se evalúa la categoría principal de la sublista para la comparación
            if categoria[j][0].lower() == categorias_unicas[i].lower():
                contador += 1
        # calculamos el promedio dividiendo la suma de precios de cada categoria por la cantidad de productos que pertenecen a esa categoria
        promedio = sumas_precios[i] // contador
        promedios_finales.append(promedio)
    # la funcion devuelve las categorias unicas y su precio promedio en 2 listas dentro de una lista para poder mostrar el informe la funcion mostrar_informe
    resultado_informe = [categorias_unicas, promedios_finales]
    return resultado_informe
#Gaspar Divano
def mostrar_informe(datos):

    titulo = datos[0]
    contenido = datos[1]
    plataforma = datos[2]
    precio = datos[3]
    stock = datos[4]
    categoria = datos[5]
    disponibilidad = datos[6]

    matriz = crear_matriz(
        titulo,
        contenido,
        plataforma,
        precio,
        stock,
        categoria,
        disponibilidad
    )

    informe_general(matriz)
    
    nombre_plat, cant_plat = calcular_plataforma_con_mas_productos(datos)
    MenusTPO.mostrar_plataforma_maxima(nombre_plat, cant_plat)

    resultado_informe_precios_promedios = calcular_precios_promedio(datos)
    MenusTPO.mostrar_informe_precios_promedio(resultado_informe_precios_promedios)

    matriz_numeros = calcular_informe_matricial(datos)
    MenusTPO.mostrar_informe_matricial(matriz_numeros, datos[9], datos[10])

# =========================================================================
# HERRAMIENTAS: AUXILIARES Y VALIDACIONES GENERALES
# =========================================================================
# Funciones sueltas que usan todos los módulos (buscar_indice, convertir_categorias_a_texto, etc.).

#inicializamos colorama para poder usar colores en la consola y mejorar la experiencia del usuario. 
# Se utiliza Fore para el color del texto, Back para el color de fondo y Style para estilos como negrita o texto normal. 
# Con autoreset=True, después de cada impresión, el color vuelve al predeterminado automáticamente.
def colorear_input(mensaje,color):#solo los dos colores que usamos son rojo y amarillo, si se ingresa otro color se muestra el mensaje sin color
    if color.lower() == "rojo":
        return input(Fore.RED + Style.BRIGHT + mensaje + Style.NORMAL)
    elif color == "amarillo":
        return input(Fore.YELLOW + Style.BRIGHT + mensaje + Style.NORMAL)
    else:
        return input(mensaje)

def imprimir_error(mensaje):
    print(Fore.RED + Style.BRIGHT + "[ERROR]" + Style.NORMAL + mensaje)#FORE.RED para texto rojo, Style.BRIGHT para negrita, Style.NORMAL para volver a texto normal después del mensaje de error

def imprimir_importante(mensaje):
    print(Fore.GREEN + Style.BRIGHT + mensaje)

def imprimir_informacion(mensaje):
    print(Fore.WHITE + Style.BRIGHT +  mensaje)
#Ignacio Diaz
def generar_indice_aleatorio_lista(lista):
    indice = random.randint(0, len(lista) - 1)
    return indice
#Tomas Ruano
def buscar_indice(lista, valor):
    indice = -1
    for i in range(len(lista)):
        if lista[i].lower() == valor.lower():
            indice = i
            break
    return indice
#Tomas Ruano
def existe_en_lista(lista, valor):
    encontrado = False
    i = 0

    while i < len(lista) and encontrado == False:
        if lista[i].lower() == valor.lower():
            encontrado = True
        i += 1

    return encontrado
#Agustin Fani
def producto_duplicado(datos, titulo_buscado):
    titulos = datos[0]

    duplicado = False
    i = 0

    while i < len(titulos) and duplicado == False:
        if titulos[i].lower() == titulo_buscado.lower():
            duplicado = True
        i += 1

    return duplicado
#Tomas Ruano
def ingresar_entero_no_negativo(msg):
    valor = input(msg)

    while valor.isdigit() == False:
        valor = colorear_input("Error. Ingrese un numero entero positivo: ", "rojo")

    return int(valor)
#Ignacio Diaz
def ingresar_float_positivo(msg):
    valor = input(msg)
    valido = False

    while valido == False:

        puntos = 0
        i = 0
        es_numero = True

        while i < len(valor) and es_numero == True:

            if valor[i] == ".":
                puntos += 1
                if puntos > 1:
                    es_numero = False

            elif valor[i].isdigit() == False:
                es_numero = False

            i += 1

        if es_numero == True and len(valor) > 0:
            valido = True
        else:
            valor = colorear_input("Ingrese un precio valido: ", "rojo")

    return float(valor)
#Tomas Sobrino
def ingresar_opcion_valida(msg, opciones):
    imprimir_importante("Opciones disponibles:")

    i = 0
    while i < len(opciones):
        imprimir_informacion(f"- {opciones[i]}")
        i += 1

    valor = input(msg)

    while existe_en_lista(opciones, valor) == False:
        imprimir_error("Opcion invalida. Debe elegir una de las opciones mostradas.")
        valor = colorear_input(msg, "rojo")

    return valor