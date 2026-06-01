# Facturas CM

Aplicación de escritorio para gestionar **cotizaciones, facturas, clientes, productos, tasas de cambio y configuración fiscal**. Está construida con [Flet](https://flet.dev/) para la interfaz, SQLite como base de datos local y SQLAlchemy para el acceso a datos.

## Características principales

- Panel inicial con resumen de facturación, cotizaciones pendientes, facturas por pagar y actividad reciente.
- Gestión de facturas y cotizaciones:
  - Creación, edición, eliminación y filtrado.
  - Conversión de cotizaciones a facturas.
  - Estados de seguimiento como por enviar, enviada y pagada.
  - Descuentos por porcentaje o monto fijo.
- Administración de clientes con datos fiscales, cuentas, teléfono y correo.
- Administración de productos con precio, proveedor, peso, moneda y tasa fiscal.
- Configuración del vendedor/emisor, tasas de cambio para CUP, MLC y MXN, tasa fiscal y notas de términos.
- Generación de PDF mediante plantillas HTML/Jinja2 y `wkhtmltopdf`.
- Base de datos SQLite incluida para uso local.

## Tecnologías

- Python
- Flet
- SQLite
- SQLAlchemy
- Jinja2
- pdfkit
- wkhtmltopdf

## Estructura del proyecto

```text
.
├── main.py                         # Punto de entrada de la aplicación Flet
├── router.py                       # Navegación entre vistas
├── controller.py                   # Lógica de negocio y acceso a datos
├── models.py                       # Modelos SQLAlchemy y conexión SQLite
├── flet_base.py                    # Import centralizado de Flet
├── facturas.db                     # Base de datos SQLite local
├── requirements.txt                # Dependencias de Python
├── assets/                         # Imágenes, iconos y fuentes
├── pages/                          # Pantallas y controles de la interfaz
│   ├── inicio.py
│   ├── factura.py
│   ├── formulario_factura.py
│   ├── clientes.py
│   ├── productos.py
│   ├── configuracion.py
│   └── common_controls/
├── pdfmaker/                       # Renderizado de documentos PDF
│   ├── pdf_render.py
│   └── template1/
└── utils/                          # Utilidades de colores y validación
```

## Requisitos previos

- Python 3.10 o superior recomendado.
- `pip` y `venv`.
- `wkhtmltopdf` instalado y disponible en el `PATH` para generar PDF.

### Instalar wkhtmltopdf

#### Windows

1. Descarga el instalador desde <https://wkhtmltopdf.org/downloads.html>.
2. Instálalo en una ruta estándar, por ejemplo:
   - `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`
3. Agrega la carpeta `bin` al `PATH` si la aplicación no lo detecta automáticamente.

#### Linux

```bash
sudo apt update
sudo apt install wkhtmltopdf
```

> Nota: en algunas distribuciones puede ser necesario instalar dependencias gráficas adicionales para que `wkhtmltopdf` funcione correctamente.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Facturas
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   ```

   En Windows:

   ```bash
   .venv\Scripts\activate
   ```

   En Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta la aplicación con:

```bash
python main.py
```

La ventana principal se abrirá con el panel de inicio. Desde el menú lateral puedes acceder a:

- **Inicio**: resumen general y actividad reciente.
- **Cotizaciones**: listado, filtros y creación de cotizaciones.
- **Facturas**: listado, filtros, creación y seguimiento de facturas.
- **Clientes**: alta, edición, búsqueda y eliminación de clientes.
- **Productos**: alta, edición, búsqueda y eliminación de productos.
- **Configuración**: datos del vendedor, tasas de cambio, tasa fiscal y notas.
- **Acerca de**: información de la aplicación.

## Generación de PDF

La aplicación genera documentos PDF usando:

- Plantillas HTML ubicadas en `pdfmaker/template1/`.
- Renderizado con Jinja2.
- Conversión HTML a PDF mediante `pdfkit` y `wkhtmltopdf`.

Si al generar un PDF aparece un error indicando que `wkhtmltopdf` no está instalado o no se encuentra en el `PATH`, revisa la sección de requisitos previos.

## Base de datos

El proyecto usa SQLite mediante el archivo `facturas.db`. Los modelos principales son:

- `Cliente`
- `Vendedor`
- `Producto`
- `Factura`
- `DetalleFactura`
- `Tasa`
- `Config`
- `MetodoPago`
- `Estado`
- `Tipo`

> Recomendación: realiza una copia de seguridad de `facturas.db` antes de modificar datos sensibles, migrar el proyecto o ejecutar cambios en la estructura de tablas.

## Notas

- La aplicación está pensada para uso local/escritorio.
- Las tasas de cambio y los datos del vendedor se administran desde la pantalla de configuración.
- El archivo de dependencias puede contener versiones fijadas para reproducir el entorno original del proyecto.
