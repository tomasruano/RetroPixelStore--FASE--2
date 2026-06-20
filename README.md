# RetroPixel Store

Sistema de gestión de productos de entretenimiento desarrollado en Python.

---

## Objetivo

El propósito del programa es centralizar la administración de películas y videojuegos, permitiendo registrar, modificar, eliminar y visualizar productos para facilitar el control del inventario de la tienda.

---

## Funcionalidades

Las principales funcionalidades implementadas son:

* Alta de productos mediante carga manual o aleatoria.
* Baja de productos con validación de eliminación.
* Modificación de productos existentes.
* Visualización general del catálogo.
* Asociación de múltiples categorías por producto.
* Alta de nuevas categorías durante el registro.
* Informe de precio promedio por categoría.
* Informe de plataforma con mayor cantidad de productos.
* Informe matricial de productos por categoría y disponibilidad.
* Interfaz con colores para mejorar la experiencia de uso.

---

## Requisitos

Para ejecutar el proyecto se requiere:

* Python 3.x
* colorama

---

## Instalación

1. Descargar o clonar el proyecto.
2. Abrir una terminal.
3. Ubicarse en la carpeta del proyecto.
4. Instalar las dependencias ejecutando:

```bash
uv pip install colorama
```

---

## Ejecución

Ejecutar el siguiente comando:

```bash
python mainTPO.py
```

---

## Estructura del Proyecto

```text
RetroPixelStore/
│
├── mainTPO.py
├── FuncionesTPO.py
├── DatosTPO.py
├── MenusTPO.py
└── README.md
```

---

## Organización del Código

### mainTPO.py

Contiene el programa principal y controla el flujo general de ejecución mediante un menú interactivo.

Funciones principales:

* Inicialización de los datos del sistema.
* Ejecución del menú principal.
* Control de las operaciones de alta, baja, modificación e informe.

---

### FuncionesTPO.py

Contiene la lógica principal del sistema.

Incluye funciones para:

#### Registro de productos

* Registro manual de productos.
* Registro aleatorio de productos.
* Generación de datos aleatorios.
* Validación de títulos duplicados.
* Selección y alta de categorías durante el registro.
* Asociación de múltiples categorías por producto.

#### Eliminación de productos

* Verificación de productos eliminables.
* Confirmación de eliminación.
* Eliminación segura de registros.

#### Modificación de productos

* Búsqueda de productos por título.
* Selección de atributos a modificar.
* Actualización de información.

#### Informe General

* Conversión de listas paralelas en una matriz.
* Ordenamiento burbuja por stock.
* Visualización tabulada de productos.
* Informe de precio promedio por categoría.
* Informe de plataforma con mayor cantidad de productos.
* Informe matricial de productos por categoría y disponibilidad.

#### Funciones auxiliares

* Búsqueda secuencial.
* Validación de enteros.
* Validación de números reales.
* Validación de opciones.
* Verificación de existencia en listas.
* Almacenamiento de nuevos productos.
* Impresión con colores en consola.

---

### DatosTPO.py

Contiene:

* Los productos precargados en el sistema.
* Las listas paralelas utilizadas para almacenar la información.
* Las opciones válidas para cada atributo.
* Los datos utilizados para la generación aleatoria de productos.

---

### MenusTPO.py

Contiene las funciones encargadas de mostrar los distintos menús utilizados por el sistema.

Incluye:

* Menú principal.
* Menú de modificación de atributos.
* Menú de selección de categorías.
* Visualización de informes estadísticos.

---

## Tecnologías Utilizadas

* Python
* random
* colorama

---

## Conceptos de Programación Aplicados

Durante el desarrollo se utilizaron los siguientes conceptos:

* Variables
* Funciones
* Modularización
* Parámetros
* Retorno de valores
* Listas
* Listas paralelas
* Listas de listas (categorías múltiples por producto)
* Matrices
* Estructuras condicionales
* Ciclos repetitivos
* Validación de datos
* Búsqueda secuencial
* Ordenamiento burbuja
* Generación aleatoria de datos
* Manipulación de listas mediante append() y pop()
* Informes estadísticos
* Matriz de conteo
* Interfaz con colores en consola

---

## Integrantes del Equipo

* Tomas Ruano
* Gaspar Divano
* Ignacio Diaz
* Tomas Sobrino
* Agustin Fani

---

## Distribución de Tareas

### Tomas Ruano

* Registro manual de productos.
* Registro aleatorio de productos.
* Funciones de búsqueda y validación.
* Control de títulos duplicados.

### Gaspar Divano

* Creación de datos iniciales.
* Generación del informe general.
* Conversión de listas paralelas a matriz.
* Ordenamiento burbuja.
* Selección de categorías y alta de nuevas categorías.
* Informe matricial de productos por categoría y disponibilidad.
* Informe de plataforma con mayor cantidad de productos.

### Ignacio Diaz

* Menú principal.
* Flujo principal del programa.
* Validación de números reales.
* Funciones auxiliares para carga de productos.
* Verificación de categorías duplicadas en producto.

### Tomas Sobrino

* Modificación de productos.
* Aplicación de cambios en atributos.
* Validación de opciones.
* Almacenamiento de productos.
* Informe de precio promedio por categoría.

### Agustin Fani

* Eliminación de productos.
* Verificación de productos eliminables.
* Eliminación por índice.
* Obtención de datos para generación aleatoria.
* Control de productos duplicados.

---

## Decisiones de Diseño

* Se separó el proyecto en módulos independientes para mejorar la organización y mantenimiento del código.
* Se utilizaron listas paralelas para almacenar la información de los productos.
* Se implementó una función propia de búsqueda debido a la restricción de no utilizar index().
* Se validaron todas las entradas del usuario mediante estructuras repetitivas.
* Se impidió el registro de productos con títulos duplicados.
* Se creó una matriz temporal para generar el informe sin modificar las listas originales.
* Se implementó un ordenamiento burbuja para mostrar los productos según su stock disponible.
* Se utilizó una lista de listas para asociar múltiples categorías a cada producto.
* Se permite registrar nuevas categorías durante el alta de un producto, agregándolas de forma persistente al sistema.
* Se utilizó colorama para mostrar mensajes de error en rojo, títulos en verde e información en color normal.

---

## Licencia

Proyecto académico desarrollado para la asignatura Pensamiento Computacional, Algoritmia y Programación.

Su finalidad es exclusivamente educativa.
