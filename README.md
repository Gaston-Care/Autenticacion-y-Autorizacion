# Autenticacion-y-Autorizacion

Es un proyecto Django para gestionar un Blog de Publicaciones. El cual permite crear publicaciones, ver publicaciones, ver publicaciones en detalle, editar publicaciones propias y eliminar publicaciones si tienes los permisos adecuados.

## Requisitos

- Python 3.10.14
- Django 4.2(especificado en el archivo 'requirements.txt')

## Instalacion

1. **Clonar el repositorio**:
En la terminal:
   git clone https://github.com/Gaston-Care/Autenticacion-y-Autorizacion

2. **Navegar al directorio del proyecto**:
    cd Autenticacion-y-Autorizacion

3. **Crear un entorno virtual**:
    virtualenv -p /usr/bin/python3.10 nombre_del_entorno

4. **Activar el entorno virtual**:

    - En Windows: .\nombre_del_entorno\Scripts\activate

    - En macOS/Linux: source nombre_del_entorno/bin/activate

5. **Instalar las dependencias**:
    pip install -r requirements.txt

6. **Realizar las migraciones a la base de datos**:
    python manage.py migrate

7. **Correr el Servidor**:
    python manage.py runserver

8. **Acceder a la Aplicacion**:
    Abre el navegador y visita http://127.0.0.1:8000/

## Uso y Funcionalidad
- home: Aparecera una barra de navegacion, Seleccione lo que desea hacer.
- Crear publicación: Ve a la sección correspondiente para crear una nueva Publicación.
- Ver publicaciones: Ve a la sección de ver publicaciones para poder ver las publicaciones.
- Ver detalles de publicacion: Ve a la sección correspondiente para ver la publicación en detalle.
- Editar publicación: Ve a la sección correspondiente para editar la publicación.
- Eliminar publicación: ve a la sección correspondiente para eliminar la publicación.

## Contacto
    gecare@udc.edu.ar - jfsassenberg@udc.edu.ar - ggvega@udc.edu.ar - vnbravo@udc.edu.ar
