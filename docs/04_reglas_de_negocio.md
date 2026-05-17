# 4. Reglas de Negocio

Este documento define las políticas operativas, restricciones lógicas y directrices comerciales que rigen el comportamiento del "Sistema de Gestión y Catálogo Web para Emprendimientos". Estas reglas son el núcleo de la lógica de la aplicación y deben ser programadas (validadas) tanto en el panel administrativo (Frontend) como en el servidor (Backend/Base de datos).

---

## 4.1 Reglas sobre la Gestión de Productos (RN-P)

*   **RN-P01 - Integridad de Registro:** Para que un producto pueda ser creado o actualizado exitosamente en el sistema, es de carácter obligatorio completar los siguientes campos: `Nombre del Producto`, `Categoría`, `Precio de Venta` y `Stock Actual`. La ausencia de cualquiera de estos datos provocará el rechazo de la transacción.
*   **RN-P02 - Validación Estricta de Precios:** El sistema debe asegurar que el precio de venta ingresado sea un valor numérico real, estrictamente mayor que cero (`Precio > 0.00`). No se permiten precios negativos ni la publicación de artículos con valor cero (gratuitos).
*   **RN-P03 - Validación de Inventario Inicial:** La cantidad de stock asignada durante la creación o actualización de un producto debe ser un número entero mayor o igual a cero (`Stock >= 0`). No se aceptarán cantidades negativas o fraccionadas.
*   **RN-P04 - Nomenclatura Única:** Para evitar inconsistencias, el sistema no permitirá registrar dos productos con exactamente el mismo nombre activo dentro de la base de datos. Si se detecta un duplicado, se exigirá agregar una variación (Ej. *Zapatos Modelo X - Talla 40*).

---

## 4.2 Reglas sobre el Control de Inventario y Ventas (RN-I)

*   **RN-I01 - Prohibición de Sobreventa (Stock Negativo):** El sistema bloqueará tajantemente el registro de cualquier venta si la cantidad de artículos a descontar es superior al stock actual del producto. El inventario en sistema jamás podrá ser inferior a cero.
*   **RN-I02 - Descuento en Tiempo Real:** En el instante en que el Administrador confirma y guarda una venta, el inventario de los productos involucrados debe reducirse automáticamente de forma transaccional.
*   **RN-I03 - Umbral de Alerta de Escasez:** Se establece una política de "Stock Bajo" cuando las existencias de un producto llegan a `5 unidades o menos`. Al alcanzar este umbral, el sistema debe disparar una alerta visual (color amarillo/rojo) en el Dashboard administrativo.

---

## 4.3 Reglas sobre la Visibilidad del Catálogo Público (RN-V)

*   **RN-V01 - Transparencia de Disponibilidad (Agotados):** Cuando el inventario de un producto llega a `0`, el producto **no desaparecerá** del catálogo público automáticamente. Seguirá siendo visible para que el cliente conozca la oferta del negocio, pero se mostrará con un filtro visual atenuado y una etiqueta inamovible de "AGOTADO", impidiendo falsas expectativas.
*   **RN-V02 - Ocultamiento Lógico Manual:** El administrador podrá marcar un producto con el estado "Inactivo" en cualquier momento. Un producto inactivo dejará de renderizarse inmediatamente en el catálogo web público, sin importar si tiene stock disponible o no.
*   **RN-V03 - Estética del Catálogo (Imagen por Defecto):** En caso de que el administrador decida no subir una fotografía al momento de crear un artículo, el sistema aplicará automáticamente una imagen "Placeholder" (Imagen no disponible) con el logotipo del emprendimiento, garantizando que el diseño de la cuadrícula del catálogo público no se rompa ni se vea poco profesional.
