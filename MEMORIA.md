# 1. Descripción del proyecto y objetivos

## Contexto y Alcance
El sistema desarrollado consiste en una **Gestión de Tienda** (`PEC2Python`).
Su alcance abarca la administración del inventario (altas, bajas, modificaciones y consultas de productos) y el procesamiento de ventas. El objetivo es ofrecer una herramienta de escritorio eficiente que centralice la operativa diaria de un comercio, garantizando la persistencia de los datos.

## Reglas de Negocio y Operativa
El sistema se rige por las siguientes reglas fundamentales:
*   **Inventario**:
    *   Todo producto debe tener un **precio** y **stock** mayor o igual a cero.
    *   Los productos se identifican de manera única en la base de datos.
*   **Ventas**:
    *   Para realizar una venta, el sistema valida previamente la disponibilidad de **stock**.
    *   Al confirmar la venta, el stock se descuenta automáticamente y se registra la transacción con estado "COMPLETADA".
*   **Operativa de Datos**:
    *   La información persiste localmente en una base de datos **SQLite**.
    *   Se permite la **importación y exportación** masiva de catálogos mediante archivos JSON.

## Objetivos Técnicos de la PEC
Este proyecto busca demostrar la aplicación práctica de:
1.  **Arquitectura MVC**: Separación clara entre Modelos (datos), Vistas (interfaz de consola) y Controladores (lógica).
2.  **Persistencia de Datos**: Conexión y gestión robusta utilizando `sqlite3`.
3.  **Calidad de Código**: Implementación de buenas prácticas en Python (Type Hinting, manejo de excepciones).

# 2. Requisitos y entorno

## Tecnologías y versiones
Para el correcto funcionamiento del sistema `PEC2Python`, se requiere el siguiente entorno:

*   **Lenguaje de Programación**: Python 3.12 o superior.
    *   Se utiliza para toda la lógica de backend, scripting y manejo de archivos.
*   **Base de Datos**: SQLite 3.
    *   Integrada nativamente en Python mediante el módulo `sqlite3`, no requiere instalación de servidor externo.
*   **Librerías Estándar**:
    *   `dataclasses`: Para la definición de modelos de datos.
    *   `typing`: Para el tipado estático (Type Hinting).
    *   `os`, `sys`, `json`: Para operaciones del sistema y manejo de archivos.
*   **Sistema Operativo**: Multiplataforma (Windows, Linux, macOS).
*   **IDE Recomendado**: PyCharm, VS Code o cualquier editor compatible con Python.

# 3. Estructura del proyecto (paquetes y clases)

## Estructura Visual
```
PEC2Python
│   export_data.json
│   README.md
│   store.db
│   
├───resources
│       schema.sql
│       
└───src
    │   Main.py
    │   
    ├───controllers
    │       cliente_controller.py
    │       data_controller.py
    │       inventario_controller.py
    │       menu_controller.py
    │       venta_controller.py
    │       
    ├───database
    │       db_manager.py
    │       
    ├───models
    │       cliente.py
    │       item_venta.py
    │       producto.py
    │       venta.py
    │       
    ├───repository
    │       cliente_repository.py
    │       data_repository.py
    │       inventario_repository.py
    │       venta_repository.py
    │       
    ├───service
    │       cliente_service.py
    │       data_service.py
    │       inventario_service.py
    │       venta_service.py
    │       
    ├───utils
    │       utils.py
    │       
    └───views
            cliente_view.py
            data_view.py
            inventario_view.py
            menu_view.py
            venta_view.py
```

## Descripción de Paquetes y Clases

### `src.controllers`
Contiene la lógica de control que coordina las vistas y los servicios.
*   **`ClienteController`**: Gestiona el flujo de administración de clientes.
*   **`InventarioController`**: Coordina las operaciones de alta y modificación de productos.
*   **`VentaController`**: Maneja el proceso de venta, validación y confirmación.
*   **`DataController`**: Controla la importación y exportación de datos.
*   **`MenuController`**: Gestiona el menú principal y la navegación.

### `src.models`
Define las estructuras de datos (DTOs) utilizando `dataclasses`.
*   **`Producto`**: Representa un artículo del inventario (id, nombre, precio, stock).
*   **`Venta`**: Representa una transacción de venta (id, fecha, total, items).
*   **`Cliente`**: Datos de clientes registrados.
*   **`ItemVenta`**: Detalle de cada producto dentro de una venta.

### `src.views`
Gestiona la interacción con el usuario a través de la consola.
*   **`VentaView`**: Muestra menús de ventas y solicita datos de compra.
*   **`InventarioView`**: Formularios para productos e informes de stock.
*   **`MenuView`**: Menú principal del sistema.

### `src.repository`
Capa de acceso a datos (DAO), ejecuta las sentencias SQL contra SQLite.
*   Cada repositorio (`InventarioRepository`, `VentaRepository`, etc.) contiene métodos CRUD (Create, Read, Update, Delete) específicos para su entidad.

### `src.service`
Capa de lógica de negocio, realiza validaciones antes de llamar a los repositorios.
*   **`VentaService`**: Valida stock disponible antes de registrar una venta y calcula totales.
*   **`InventarioService`**: Valida que precios y stocks no sean negativos.

### `src.database`
*   **`DBManager`**: Singleton encargado de abrir y cerrar la conexión con `store.db` y crear las tablas iniciales.

### `src.utils`
*   **`Utils`**: Funciones auxiliares para captura segura de datos por teclado (enteros, flotantes) y limpieza de pantalla.

# 4. Diseño lógico de la base de datos

## Modelo Relacional

La base de datos se ha implementado utilizando **SQLite** bajo el esquema definido en `resources/schema.sql`.

### Tablas y Atributos

1.  **`productos`**
    *   Almacena el catálogo de artículos disponibles para la venta.
    *   **PK**: `id` (INTEGER AUTOINCREMENT).
    *   **Atributos**: `nombre` (TEXT), `descripcion` (TEXT), `precio` (REAL), `stock` (INTEGER), `categoria` (TEXT).
    *   **Restricciones**: `precio` >= 0, `stock` >= 0.

2.  **`clientes`**
    *   Registra la información de los usuarios/compradores.
    *   **PK**: `id` (INTEGER AUTOINCREMENT).
    *   **Atributos**: `nombre` (TEXT), `email` (TEXT UNIQUE), `saldo` (REAL).

3.  **`ventas`**
    *   Representa la cabecera de una transacción de venta.
    *   **PK**: `id` (INTEGER AUTOINCREMENT).
    *   **FK**: `cliente_id` referencia a `clientes(id)`.
    *   **Atributos**: `total` (REAL), `estado` (TEXT, default 'COMPLETADA').

4.  **`lineas_venta`**
    *   Detalla los productos incluidos en cada venta (tabla intermedia).
    *   **PK**: `id` (INTEGER AUTOINCREMENT).
    *   **FK**: `venta_id` referencia a `ventas(id)` (ON DELETE CASCADE).
    *   **FK**: `producto_id` referencia a `productos(id)`.
    *   **Atributos**: `cantidad` (INTEGER > 0), `subtotal` (REAL >= 0).

## Cardinalidades

*   **Clientes - Ventas (1:N)**: Un cliente puede realizar múltiples compras. Cada venta está vinculada obligatoriamente a un único cliente.
*   **Ventas - Líneas de Venta (1:N)**: Una venta puede contener múltiples líneas de detalle.
*   **Productos - Líneas de Venta (1:N)**: Un producto puede aparecer en múltiples transacciones.

## Normalización

*   **Primera Forma Normal (1FN)**: Todos los atributos son atómicos y no existen grupos repetitivos. Cada tabla tiene una clave primaria definida.
*   **Segunda Forma Normal (2FN)**: Todas las columnas no clave dependen funcionalmente de la clave primaria completa.
*   **Tercera Forma Normal (3FN)**: No existen dependencias transitivas entre columnas no clave.
*   **Tercera Forma Normal (3FN)**: No existen dependencias transitivas entre columnas no clave.
    *   *Nota*: Aunque el campo `subtotal` en `lineas_venta` podría calcularse (`cantidad` * `precio`), se ha decidido persistir para mantener el histórico del precio en el momento de la venta y mejorar el rendimiento de consultas de totales, sin violar la integridad lógica del negocio.

# 5. Casos de uso

A continuación se detallan los 10 casos de uso más relevantes del sistema.

| ID | Nombre | Descripción | Pre-condiciones | Salida |
| :--- | :--- | :--- | :--- | :--- |
| **UC-01** | **Alta de Producto** | Registrar un nuevo artículo en el inventario con sus atributos básicos. | Datos válidos (precio/stock >= 0). | Mensaje de confirmación en consola. |
| **UC-02** | **Listar Inventario** | Visualizar todos los productos registrados con su stock y precio actual. | Base de datos inicializada. | Tabla con la lista de productos. |
| **UC-03** | **Modificar Producto** | Actualizar los datos (precio, stock, nombre) de un producto existente. | El producto debe existir (ID válido). | Confirmación de actualización. |
| **UC-04** | **Eliminar Producto** | Dar de baja un artículo del catálogo. | El producto debe existir. | Mensaje de éxito al borrar. |
| **UC-05** | **Alta de Cliente** | Registrar un nuevo cliente en el sistema. | Email único, saldo inicial >= 0. | Mensaje de cliente creado. |
| **UC-06** | **Listar Clientes** | Consultar la cartera de clientes registrados. | - | Lista de clientes en pantalla. |
| **UC-07** | **Nueva Venta** | Registrar una transacción de venta vinculada a un cliente. | Cliente existe, stock suficiente. | Venta creada y stock descontado. |
| **UC-08** | **Historial Ventas** | Consultar el listado histórico de ventas realizadas. | - | Tabla con ID, Total, Estado y Cliente. |
| **UC-09** | **Exportar Datos** | Generar un archivo JSON con la información actual de la base de datos. | Permisos de escritura en disco. | Archivo `export_data.json` generado. |
| **UC-10** | **Importar Datos** | Cargar datos masivos desde un archivo JSON externo. | Archivo JSON válido y existente. | Base de datos actualizada con los nuevos datos. |

