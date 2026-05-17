# 5. Arquitectura y Modelo de Base de Datos

En este documento se define la estructura técnica del sistema, abarcando desde el diseño de la arquitectura de software hasta la estructura del modelo relacional de la base de datos que almacenará la información del emprendimiento.

---

## 5.1 Arquitectura del Sistema

El "Sistema de Gestión y Catálogo Web" se construirá bajo el patrón arquitectónico **Cliente-Servidor (Client-Server Architecture)**, apoyado en el patrón de diseño **MVC (Modelo-Vista-Controlador)** que proveen los frameworks modernos. 

La plataforma estará dividida lógicamente en tres capas principales:

1.  **Capa de Presentación (Frontend / Cliente):** 
    *   **Tecnologías:** HTML5 (semántico), CSS3 (diseño responsivo y estético) y JavaScript (Vanilla JS para validaciones y peticiones asíncronas).
    *   **Función:** Es la interfaz con la que interactúan tanto los clientes (catálogo público) como el administrador (panel de control). Se encarga de mostrar la información de forma amigable y capturar los eventos del usuario.
2.  **Capa de Lógica de Negocio (Backend / Servidor):** 
    *   **Tecnologías:** Python utilizando el micro-framework **Flask**.
    *   **Función:** Actúa como el cerebro del sistema. Recibe las peticiones HTTP del cliente, procesa las reglas de negocio (validar stock, calcular totales), interactúa con la base de datos y devuelve respuestas (HTML renderizado a través de plantillas Jinja2 o datos en formato JSON).
3.  **Capa de Acceso a Datos (Base de Datos):** 
    *   **Tecnologías:** Base de datos relacional SQL (ej. SQLite para desarrollo local y PostgreSQL/MySQL para producción) mapeada a través de un ORM (Object-Relational Mapping) como SQLAlchemy.
    *   **Función:** Almacena de manera persistente, segura e íntegra toda la información del catálogo, usuarios y ventas.

---

## 5.2 Modelo de Base de Datos (Diccionario de Datos)

El sistema utilizará un modelo relacional normalizado. A continuación se definen las entidades principales (tablas), sus atributos, tipos de datos y restricciones.

### Entidad: `Usuarios` (Administradores del sistema)
Almacena las credenciales de los dueños del emprendimiento con acceso al panel de control.

| Campo | Tipo de Dato | Llave | Descripción y Restricciones |
| :--- | :--- | :--- | :--- |
| `id_usuario` | Integer | **PK** | Identificador único autoincremental. |
| `nombre_completo`| Varchar(100) | | Nombre del administrador. (Not Null) |
| `correo_email` | Varchar(150) | **UK** | Correo electrónico para el login. (Not Null, Único) |
| `password_hash` | Varchar(255) | | Contraseña encriptada por seguridad. (Not Null) |
| `fecha_creacion` | DateTime | | Fecha en la que se creó la cuenta. |

### Entidad: `Categorias`
Permite agrupar y clasificar los productos del catálogo.

| Campo | Tipo de Dato | Llave | Descripción y Restricciones |
| :--- | :--- | :--- | :--- |
| `id_categoria` | Integer | **PK** | Identificador único autoincremental. |
| `nombre` | Varchar(50) | **UK** | Nombre de la categoría (ej. "Ropa", "Accesorios"). (Not Null) |
| `descripcion` | Text | | Breve detalle opcional sobre la categoría. |

### Entidad: `Productos` (Inventario)
La entidad central del sistema que almacena la información del catálogo.

| Campo | Tipo de Dato | Llave | Descripción y Restricciones |
| :--- | :--- | :--- | :--- |
| `id_producto` | Integer | **PK** | Identificador único autoincremental. |
| `id_categoria` | Integer | **FK** | Relación con la tabla `Categorias`. |
| `nombre` | Varchar(100) | | Nombre público del artículo. (Not Null) |
| `descripcion` | Text | | Descripción detallada para el catálogo. |
| `precio_venta` | Decimal(10,2)| | Valor comercial monetario. (Not Null, > 0) |
| `stock_actual` | Integer | | Cantidad de unidades disponibles. (Not Null, >= 0) |
| `imagen_url` | Varchar(255) | | Ruta del archivo de la fotografía en el servidor. |
| `estado_activo` | Boolean | | `True` (Visible) o `False` (Oculto/Inactivo). |

### Entidad: `Ventas` (Cabecera de la transacción)
Registra los datos generales de una venta efectuada.

| Campo | Tipo de Dato | Llave | Descripción y Restricciones |
| :--- | :--- | :--- | :--- |
| `id_venta` | Integer | **PK** | Identificador único (Número de ticket). |
| `id_usuario` | Integer | **FK** | Qué administrador registró la venta. |
| `fecha_hora` | DateTime | | Momento exacto en que se concretó la venta. |
| `total_venta` | Decimal(10,2)| | Sumatoria monetaria de toda la transacción. |

### Entidad: `Detalle_Ventas`
Desglosa los productos individuales que se incluyeron dentro de una `Venta`.

| Campo | Tipo de Dato | Llave | Descripción y Restricciones |
| :--- | :--- | :--- | :--- |
| `id_detalle` | Integer | **PK** | Identificador único del renglón. |
| `id_venta` | Integer | **FK** | Relación con la cabecera `Ventas`. |
| `id_producto` | Integer | **FK** | Producto específico que fue vendido. |
| `cantidad` | Integer | | Unidades vendidas de este producto. (Not Null, > 0) |
| `precio_unitario`| Decimal(10,2)| | Precio del producto al momento exacto de la venta (evita alteraciones si el precio cambia en el futuro). |

> **Nota de Relaciones:** Un *Usuario* puede registrar muchas *Ventas* (1:N). Una *Categoría* puede tener muchos *Productos* (1:N). Una *Venta* se compone de muchos *Detalles de Venta* (1:N), y un *Producto* puede aparecer en muchos *Detalles de Venta* (1:N).
