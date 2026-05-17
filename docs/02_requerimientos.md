# 2. Análisis y Requerimientos

En esta sección se definen las capacidades técnicas e interacciones que el sistema debe proveer para cumplir con los objetivos planteados. Se dividen en Requerimientos Funcionales (lo que el sistema debe hacer) y Requerimientos No Funcionales (cómo debe comportarse).

---

## 2.1 Requerimientos Funcionales (RF)

Los requerimientos funcionales han sido agrupados por módulos operativos para facilitar su trazabilidad, comprensión y posterior desarrollo.

### Módulo de Autenticación y Seguridad
| ID | Nombre | Descripción | Prioridad |
|:---|:---|:---|:---:|
| **RF-01** | Inicio de sesión (Login) | El sistema debe permitir al administrador ingresar al panel de control mediante correo electrónico y contraseña. | Alta |
| **RF-02** | Cierre de sesión (Logout) | El sistema debe permitir al administrador finalizar su sesión activa de forma segura. | Alta |
| **RF-03** | Recuperación de credenciales | El sistema debe enviar un enlace de recuperación al correo registrado en caso de olvido de contraseña. | Media |

### Módulo de Gestión de Inventario y Productos
| ID | Nombre | Descripción | Prioridad |
|:---|:---|:---|:---:|
| **RF-04** | Registro de Producto | El administrador debe poder crear nuevos productos especificando: nombre, descripción, precio, categoría, stock inicial e imágenes. | Alta |
| **RF-05** | Actualización de Producto | El administrador debe poder editar la información, precio o fotografías de un producto existente. | Alta |
| **RF-06** | Baja u Ocultamiento | El sistema debe permitir al administrador eliminar o inhabilitar un producto para que deje de mostrarse en el catálogo público. | Alta |
| **RF-07** | Gestión de Categorías | El sistema debe proveer opciones para crear, editar y eliminar categorías que agrupen los productos del negocio. | Media |

### Módulo de Gestión de Ventas
| ID | Nombre | Descripción | Prioridad |
|:---|:---|:---|:---:|
| **RF-08** | Registro de Venta | El administrador debe poder registrar manualmente una nueva venta, indicando los artículos y cantidades vendidas. | Alta |
| **RF-09** | Actualización de Stock | Al confirmar una venta, el sistema debe descontar automáticamente del inventario las cantidades vendidas. | Alta |
| **RF-10** | Historial de Transacciones | El administrador debe tener acceso a un listado con el registro de todas las ventas, con opciones de filtrado por fecha. | Alta |

### Módulo de Visualización del Catálogo (Cara al Cliente)
| ID | Nombre | Descripción | Prioridad |
|:---|:---|:---|:---:|
| **RF-11** | Catálogo Principal | Los clientes deben poder visualizar una cuadrícula con todos los productos disponibles y sus respectivos precios, sin necesidad de registro. | Alta |
| **RF-12** | Filtros de Búsqueda | El catálogo público debe incluir un menú para filtrar productos por categoría y barra de búsqueda por nombre o palabra clave. | Alta |
| **RF-13** | Detalles del Producto | Al seleccionar un producto, el cliente debe acceder a una vista ampliada con su descripción completa, galería de fotos e indicador de disponibilidad ("En Stock" / "Agotado"). | Alta |

### Módulo de Reportes (Dashboard)
| ID | Nombre | Descripción | Prioridad |
|:---|:---|:---|:---:|
| **RF-14** | Resumen de Rendimiento | El panel de inicio del administrador (Dashboard) debe mostrar métricas clave: total de ventas mensuales, ingresos generados y cantidad total de productos. | Media |
| **RF-15** | Alertas de Stock | El sistema debe notificar visualmente en el panel administrativo qué productos tienen un stock inferior a un límite predefinido (ej. menos de 5 unidades). | Baja |

---

## 2.2 Requerimientos No Funcionales (RNF)

Los requerimientos no funcionales definen los atributos de calidad, rendimiento de la plataforma y las restricciones tecnológicas.

| ID | Categoría | Descripción |
|:---|:---|:---|
| **RNF-01** | **Usabilidad** | La interfaz de usuario (UI) debe ser moderna, limpia e intuitiva, asegurando que un usuario sin conocimientos técnicos pueda administrar la plataforma con una mínima curva de aprendizaje. |
| **RNF-02** | **Diseño Responsivo** | El diseño del sistema debe adaptarse a diferentes resoluciones de pantalla (Mobile-First). El catálogo público debe verse y funcionar perfectamente en smartphones, tablets y computadoras. |
| **RNF-03** | **Rendimiento** | El tiempo de respuesta de las páginas del catálogo público no debe exceder los 3 segundos en condiciones de conexión a internet estándar, para garantizar una buena retención de clientes. |
| **RNF-04** | **Seguridad** | Las contraseñas de los administradores deben estar encriptadas (ej. algoritmo Bcrypt) en la base de datos. Las rutas del backend (API) deben estar protegidas mediante tokens JWT. |
| **RNF-05** | **Compatibilidad** | La plataforma web debe ser compatible y renderizarse correctamente en las últimas versiones estables de navegadores modernos (Google Chrome, Safari, Mozilla Firefox, Microsoft Edge). |
| **RNF-06** | **Mantenibilidad** | El código fuente debe aplicar buenas prácticas de ingeniería de software (código limpio, modularización, comentarios descriptivos) facilitando su escalabilidad y futuros mantenimientos. |
