# BrandHub Studio

Plataforma web para una marca creativa o agencia digital desarrollada con Django 5.x, Bootstrap 5 y PostgreSQL/SQLite.

## Características

- **Portafolio**: Gestión de proyectos con galerías de imágenes
- **Servicios**: Planes de servicios con precios y características
- **Blog**: Publicaciones de novedades y tutoriales
- **Productos**: Productos digitales con galerías
- **Solicitudes**: Formulario de contacto y gestión de clientes
- **Dashboard**: Panel administrativo personalizado
- **Diseño**: Interfaz moderna y responsiva con Bootstrap 5

## Tecnologías

- Python 3.11+
- Django 5.x
- SQLite (desarrollo) / PostgreSQL (producción)
- Bootstrap 5
- Pillow (manejo de imágenes)
- python-decouple (variables de entorno)
- django-widget-tweaks (formularios)
- WhiteNoise (archivos estáticos)
- crispy-bootstrap5 (formularios mejorados)

## Estructura del Proyecto

```
brandhub_studio/
├── config/              # Configuración principal de Django
├── accounts/           # Autenticación de usuarios
├── core/               # Modelos base (Testimonial, SiteConfiguration)
├── portfolio/          # Gestión de proyectos de portafolio
├── services/           # Planes de servicios
├── blog/               # Blog y publicaciones
├── products/           # Productos digitales
├── inquiries/          # Solicitudes de clientes
├── dashboard/          # Panel administrativo
├── templates/          # Templates HTML
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── media/              # Archivos multimedia subidos
├── venv/               # Entorno virtual
├── manage.py           # Script de gestión de Django
├── requirements.txt    # Dependencias de Python
└── .env                # Variables de entorno
```

## Instalación

### 1. Activar el entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

**Credenciales por defecto:**
- Usuario: `maria@gmail.com`
- Contraseña: `dbmari12`

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en: http://localhost:8000

## URLs Principales

### Públicas
- `/` - Inicio
- `/portafolio/` - Portafolio de proyectos
- `/portafolio/<slug>/` - Detalle de proyecto
- `/servicios/` - Planes de servicios
- `/blog/` - Blog
- `/blog/<slug>/` - Detalle de post
- `/contacto/` - Formulario de contacto

### Privadas (requieren autenticación)
- `/panel/` - Dashboard principal
- `/panel/proyectos/` - Gestión de proyectos
- `/panel/productos/` - Gestión de productos
- `/panel/blog/` - Gestión de blog
- `/panel/solicitudes/` - Gestión de solicitudes
- `/panel/calendario/` - Calendario de publicaciones

### Autenticación
- `/login/` - Iniciar sesión
- `/logout/` - Cerrar sesión
- `/admin/` - Panel de administración de Django

## Panel de Administración Django

Accede al panel de administración Django en: http://localhost:8000/admin/

Desde aquí puedes gestionar:
- Proyectos y galerías
- Planes de servicios
- Productos y galerías
- Posts del blog
- Solicitudes de clientes
- Testimonios
- Configuración del sitio

## Datos de Prueba

Para agregar datos de prueba, puedes hacerlo desde el panel de administración Django:

1. Inicia sesión en `/admin/`
2. Crea 3 servicios: Básico, Emprendedor, Premium
3. Crea 6 proyectos de portafolio
4. Crea 4 productos o colecciones
5. Crea 4 posts de novedades
6. Crea 3 testimonios

## Configuración para Producción

1. Cambia `DEBUG=False` en el archivo `.env`
2. Configura una base de datos PostgreSQL
3. Establece un `SECRET_KEY` seguro
4. Configura `ALLOWED_HOSTS` con tu dominio
5. Ejecuta `python manage.py collectstatic`

## Colores del Tema

- Azul oscuro: `#111827`
- Azul principal: `#2563EB`
- Morado: `#7C3AED`
- Gris claro: `#F9FAFB`
- Texto oscuro: `#1F2937`

## Seguridad

- Los formularios incluyen protección CSRF
- El panel administrativo requiere autenticación
- Las imágenes se validan al subir
- Los slugs son únicos para evitar conflictos
- Variables sensibles en archivo `.env`

## Soporte

Para problemas o preguntas, consulta la documentación de Django: https://docs.djangoproject.com/

## Licencia

Este proyecto fue creado para fines educativos y de demostración.
