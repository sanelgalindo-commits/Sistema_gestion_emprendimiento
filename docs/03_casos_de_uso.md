# 3. Casos de Uso del Sistema

En esta sección se definen las interacciones formales entre los actores (usuarios) y el sistema. Estos Casos de Uso (CU) detallan los pasos específicos requeridos para lograr un objetivo particular dentro del "Sistema de Gestión y Catálogo Web para Emprendimientos".

## 3.1 Identificación de Actores

Para este proyecto, se han identificado dos actores principales que interactuarán con la plataforma:

*   👤 **Actor Principal - Administrador (Dueño del Emprendimiento):** Usuario con privilegios elevados y autenticado. Es el encargado de gestionar el inventario, registrar ventas manuales, administrar el contenido del catálogo y visualizar los reportes financieros.
*   👥 **Actor Secundario - Cliente (Usuario Público):** Visitante anónimo que accede a la plataforma web. Su objetivo principal es navegar por el catálogo, buscar productos específicos y consultar características, precios y disponibilidad.

---

## 3.2 Descripciones Detalladas de Casos de Uso

A continuación, se documentan los flujos de los dos procesos más representativos del sistema.

### CU-01: Registrar Nuevo Producto en el Catálogo
*   **Actor:** Administrador
*   **Descripción:** Permite al dueño del emprendimiento ingresar un nuevo artículo al sistema para que pase a formar parte del inventario y esté disponible para la visualización pública.
*   **Precondiciones:** El Administrador debe haber iniciado sesión exitosamente en el panel de control (Backend).
*   **Postcondiciones:** El nuevo producto queda registrado en la base de datos con su respectivo stock y, si se aprueba su visibilidad, aparece inmediatamente en el catálogo web público.

#### Flujo Principal (Escenario de Éxito)
1.  El Administrador accede al menú de navegación lateral del panel de control y selecciona "Inventario" -> "Agregar Producto".
2.  El sistema despliega un formulario interactivo vacío para el registro del artículo.
3.  El Administrador ingresa los datos obligatorios requeridos: Nombre del producto, Categoría (seleccionando desde una lista desplegable preexistente), Precio de Venta (Numérico) y Stock Inicial (Numérico).
4.  El Administrador complementa el registro con datos opcionales: Descripción detallada en formato texto y carga una o más imágenes representativas desde su dispositivo.
5.  El Administrador hace clic en el botón "Guardar Producto".
6.  El sistema valida internamente que los campos obligatorios no estén vacíos y que los formatos numéricos (como precios negativos) no contengan errores.
7.  El sistema procesa y guarda la información, subiendo las imágenes al servidor de almacenamiento.
8.  El sistema retorna un mensaje de confirmación ("Producto registrado exitosamente") y redirige al Administrador a la vista general de la lista de inventario.

#### Flujos Alternativos (Manejo de Excepciones)
*   *A1: Datos incompletos o inválidos (En Paso 6).* Si el sistema detecta la ausencia de un campo obligatorio o un formato erróneo (por ejemplo, texto en el campo de precio), interrumpe el guardado, mantiene los datos en pantalla y muestra un mensaje de alerta en rojo resaltando el campo que debe ser corregido. El flujo retorna al Paso 3.
*   *A2: Fallo al cargar la imagen (En Paso 6).* Si la imagen seleccionada supera el límite de peso máximo permitido (Ej. 5 MB) o el formato no es válido (Ej. .pdf en lugar de .jpg/.png), el sistema rechaza el archivo y solicita al Administrador que seleccione un formato optimizado.

---

### CU-02: Visualizar y Filtrar Catálogo
*   **Actor:** Cliente
*   **Descripción:** Permite a un visitante explorar la oferta comercial del emprendimiento, encontrar rápidamente lo que busca mediante filtros por categorías, y consultar los detalles específicos de un ítem.
*   **Precondiciones:** El dispositivo del Cliente debe tener conexión a internet. El servidor del sistema web debe estar operativo. (No requiere autenticación/login).
*   **Postcondiciones:** El Cliente visualiza la información de los productos y su estado actual de disponibilidad.

#### Flujo Principal (Escenario de Éxito)
1.  El Cliente ingresa a la URL pública del sistema a través del navegador web de su dispositivo (Móvil o Desktop).
2.  El sistema carga la página de inicio (Frontend) desplegando una cuadrícula principal con todos los productos activos, ordenados por los añadidos más recientemente.
3.  El Cliente localiza el panel de filtros (ubicado a la izquierda en Desktop o en un botón desplegable en Móvil) y hace clic en una Categoría específica (Ej. "Accesorios").
4.  El sistema procesa la solicitud asíncronamente (sin recargar la página entera) y actualiza la cuadrícula mostrando únicamente los ítems que pertenecen a la categoría "Accesorios".
5.  El Cliente requiere ser más específico y utiliza la "Barra de Búsqueda" superior, introduciendo una palabra clave (Ej. "Collar de plata").
6.  El sistema aplica este segundo filtro y muestra exclusivamente los productos que sean "Accesorios" Y cuyo nombre contenga "Collar de plata".
7.  El Cliente encuentra un producto de su interés y hace clic sobre su fotografía.
8.  El sistema abre la vista de "Detalle del Producto", mostrando la imagen ampliada, la descripción larga, el precio y un indicador destacado sobre su disponibilidad actual ("En Stock: 12 unidades" o "Disponible").

#### Flujos Alternativos (Manejo de Excepciones)
*   *A1: Búsqueda sin coincidencias (En Paso 4 o 6).* Si tras aplicar un filtro o realizar una búsqueda no existen productos activos en la base de datos que cumplan los criterios, el sistema limpia la cuadrícula y muestra un mensaje amigable tipo "No encontramos productos que coincidan con tu búsqueda. ¡Prueba con otras palabras!", junto a un botón para limpiar filtros y ver el catálogo completo.
*   *A2: Producto Agotado (En Paso 8).* Si el Cliente ingresa al detalle de un producto cuyo inventario interno llegó a cero, el sistema mostrará la información pero reemplazará la etiqueta de disponibilidad por un cartel rojo que indique "Agotado / Sin Stock", evitando que el cliente crea que puede adquirirlo inmediatamente.
