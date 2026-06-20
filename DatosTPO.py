# Las empezadas en "Opciones", son para que el usuario las vea al usar el menu interactivo y sepa que poner.
#Gaspar Divano
def crearDatosIniciales():
    '''  Crea y devuelve las listas de datos iniciales para el sistema de gestión de productos.
     Estas listas incluyen títulos, contenidos, plataformas, precios, stock, categorías y disponibilidades de productos, así como las opciones permitidas para cada atributo.
     Retorna: Una tupla con todas las listas de datos iniciales.'''
    # 1. Listas paralelas con los datos cargados de base en el sistema
    titulo = ["Batman", "Spider-man", "The Last Of Us II", "God Of War","Red dead redemption 2", "Cyberpunk 2077", "The witcher 3", "Uncharted 4", "Hogwarts legacy", "Resident evil village"]
    contenido = ["Pelicula", "Videojuego", "Videojuego", "Videojuego", "Videojuego", "Videojuego", "Videojuego", "Videojuego", "Videojuego", "Videojuego"]
    plataforma = ["Blu-Ray", "Playstation 5", "Playstation 5", "Playstation 5", "Xbox Series X", "PC", "PC", "Playstation 5", "Xbox Series X", "Playstation 5"]
    precio = [15000.0, 45000.0, 50000.0, 40000.0, 55000.0, 60000.0, 55000.0, 45000.0, 55000.0, 45000.0]
    stock = [5, 2, 0, 4, 3, 2, 1, 3, 2, 1]
    categoria = [["Accion"], ["Accion"], ["Aventura"], ["Accion"], ["Aventura"], ["Ciencia Ficcion"], ["Aventura"], ["Aventura"], ["Aventura"], ["Terror"]]
    disponibilidad = ["Disponible", "Disponible", "Discontinuado", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible", "Disponible"]
    
    # 2. Listas de opciones permitidas (sirven para validar que lo que escriban sea correcto)
    opciones_contenido = ["Videojuego", "Pelicula"]
    opciones_plataforma = ["Playstation 5", "Xbox Series X", "PC", "Blu-Ray", "DVD"]
    opciones_categoria = ["Accion", "Aventura", "Ciencia Ficcion", "Terror", "Deportes"]
    opciones_disponibilidad = ["Disponible", "Alquilado", "Reservado", "Discontinuado"]
    
    datos = [titulo, contenido, plataforma, precio, stock, categoria, disponibilidad,
              opciones_contenido, opciones_plataforma, opciones_categoria, opciones_disponibilidad]
    # 3. Empaquetamos todo y lo enviamos hacia el main()
    return datos
#Agustin Fani
def obtener_titulos_y_categorias():

    titulos = [
        "Minecraft",
        "Call of duty",
        "FC 26",
        "Assassin's creed valhalla",
        "Inception",
        "Spider-man: Far from home",
        "Interstellar",
        "The matrix",
        "Pulp fiction",
        "Fight club",
        "Forrest gump",
        "Harry potter y la piedra filosofal",
        "El señor de los anillos",
        "Star wars",
        "Avengers endgame",
        "Joker"
    ]

    categorias = [
        ["Otro"],
        ["Accion"],
        ["Deportes"],
        ["Aventura"],
        ["Ciencia Ficcion"],
        ["Accion"],
        ["Ciencia Ficcion"],
        ["Ciencia Ficcion"],
        ["Accion"],
        ["Accion"],
        ["Otro"],
        ["Aventura"],
        ["Aventura"],
        ["Ciencia Ficcion"],
        ["Accion"],
        ["Accion"]
    ]
    random_data = [titulos, categorias]
    return random_data