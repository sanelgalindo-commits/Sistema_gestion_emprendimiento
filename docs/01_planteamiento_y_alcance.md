# 1. Planteamiento, Objetivos y Alcance

## 1.1 Planteamiento del Problema

En la actualidad, un gran porcentaje de pequeños emprendimientos y negocios locales operan de manera informal en cuanto a la gestión de su información. La administración de inventarios, el registro de ventas y la exhibición de productos suelen realizarse mediante métodos manuales (libretas de apuntes) o herramientas ofimáticas genéricas (hojas de cálculo), lo que resulta en procesos ineficientes, propensos a errores humanos y con una alta dificultad para la toma de decisiones basada en datos.

Además, muchos de estos emprendimientos carecen de una presencia digital profesional. La venta a través de redes sociales, aunque popular, a menudo carece de un catálogo organizado y centralizado, lo que dificulta a los clientes potenciales explorar la oferta completa de productos, consultar disponibilidad en tiempo real o conocer los precios de forma autónoma. Esta falta de digitalización y automatización limita significativamente la capacidad de crecimiento, la escalabilidad del negocio y la fidelización de clientes.

Ante esta situación, se hace evidente la necesidad de una herramienta tecnológica accesible, centralizada y de fácil uso que permita a los pequeños negocios dar el salto hacia la digitalización, unificando su presencia online con su gestión operativa interna.

---

## 1.2 Objetivos

### Objetivo General
Desarrollar un "Sistema de Gestión y Catálogo Web" que permita a los pequeños emprendimientos digitalizar la exhibición de sus productos y centralizar el control operativo de sus ventas e inventario, mejorando la eficiencia administrativa y su presencia en línea.

### Objetivos Específicos
1. **Diseñar y desarrollar un catálogo web interactivo:** Proveer una interfaz pública y accesible donde los clientes puedan explorar los productos, ver detalles, precios y disponibilidad en tiempo real.
2. **Implementar un módulo de gestión de inventario (CRUD):** Permitir a los administradores del negocio crear, leer, actualizar y eliminar (CRUD) información sobre productos, categorías y stock.
3. **Desarrollar un módulo de registro y control de ventas:** Facilitar la captura de transacciones diarias, asociando los productos vendidos y actualizando el inventario de manera automática.
4. **Generar reportes básicos de rendimiento:** Proveer un panel de control (Dashboard) que muestre estadísticas clave como ventas mensuales, productos más vendidos y alertas de stock bajo.
5. **Garantizar una experiencia de usuario (UX) intuitiva y responsiva:** Asegurar que el sistema sea fácil de utilizar tanto para los clientes finales desde sus dispositivos móviles, como para los dueños del negocio al administrar la plataforma.

---

## 1.3 Alcance y Límites del Proyecto

### ¿Qué incluye el sistema? (Dentro del alcance)
El desarrollo contempla la construcción de una plataforma web dividida en dos grandes módulos:
*   **Frontend Público (Catálogo):** Una vitrina virtual para que los clientes visualicen el catálogo de productos por categorías, con buscador y detalles del artículo.
*   **Backend / Panel Administrativo:** Un área segura con autenticación (login) para el dueño del emprendimiento. Desde aquí podrá:
    *   Gestionar el catálogo (agregar fotos, descripciones, precios, stock).
    *   Registrar ventas realizadas de forma manual.
    *   Visualizar el dashboard con el resumen financiero y de inventario.

### ¿Qué NO incluye el sistema? (Fuera del alcance)
Para asegurar la viabilidad del proyecto en esta primera versión (MVP - Producto Mínimo Viable), no se contemplarán las siguientes funcionalidades:
*   **Pasarela de Pagos Online:** El sistema no procesará pagos con tarjetas de crédito/débito directamente en la web. El catálogo servirá como vitrina y los pagos se coordinarán externamente (transferencias, efectivo al entregar).
*   **Logística y Envíos Automatizados:** No habrá integraciones directas con empresas de paquetería o cálculo automático de costos de envío dinámicos.
*   **Facturación Electrónica:** El sistema registrará la venta internamente, pero no estará conectado a entidades gubernamentales (como el SRI, SUNAT, AFIP, SAT, etc.) para la emisión de facturas legales tributarias.
*   **Gestión Contable Completa:** No se manejarán conceptos avanzados como pago de nóminas, depreciación de activos o flujo de caja profundo.

### Justificación
Este alcance permite entregar una solución de alto valor que resuelve el problema central de desorganización y falta de presencia digital, manteniendo un nivel de complejidad adecuado para los plazos y recursos del presente proyecto.
