# Sistema de Gestión de Tienda (PEC2Python)

Este proyecto es una aplicación de escritorio desarrollada en Python para la gestión de inventario y ventas de una tienda. Utiliza una arquitectura MVC (Modelo-Vista-Controlador) y una base de datos SQLite para la persistencia de datos.

## Características Principales

*   **Gestión de Productos**: Alta, baja, modificación y consulta de productos.
*   **Gestión de Ventas**: Registro de ventas y asociación con productos.
*   **Persistencia de Datos**: Uso de SQLite (`store.db`) para almacenar la información de forma local.
*   **Arquitectura MVC**: Separación clara entre la lógica de negocio (Modelos/Servicios), la interfaz de usuario (Vistas) y el control de flujo (Controladores).
*   **Exportación/Importación**: Funcionalidades para manejar datos en formato JSON.

## Requisitos

*   Python 3.12+
*   Librerías estándar de Python (no requiere instalación de paquetes externos mediante pip, utiliza `sqlite3`, `dataclasses`, `typing`, etc.)

## Estructura del Proyecto

```
PEC2Python
│   README.md
│   store.db
│   
└───src
    ├───controllers   (Lógica de control)
    ├───models        (Clases de datos)
    ├───views         (Interfaz de usuario)
    ├───repository    (Acceso a datos SQL)
    ├───service       (Lógica de negocio)
    ├───database      (Conexión SQLite)
    └───utils         (Utilidades)
```

El código fuente se organiza siguiendo el patrón MVC:
*   **Controllers**: Orquestan las operaciones.
*   **Views**: Muestran información y solicitan datos al usuario.
*   **Services**: Aplican reglas de negocio (validaciones).
*   **Repositories**: Interactúan directamente con la base de datos.
*   **Models**: Estructuras de datos puras.


## Instalación y Uso

1.  **Clonar el repositorio** o descargar el código fuente.

2.  **Ejecutar la aplicación**:
    Abre una terminal en la raíz del proyecto (donde se encuentra este `README.md`) y ejecuta el siguiente comando:

    ```bash
    python src/Main.py
    ```

    La aplicación iniciará y mostrará el menú principal en la consola.

## Base de Datos

La aplicación utiliza un archivo de base de datos llamado `store.db` que se creará automáticamente en la raíz del proyecto si no existe, utilizando el esquema definido en `resources/schema.sql`.
