# Proyecto Blog en Django

Este proyecto es un blog desarrollado utilizando Django en Visual Studio Code, aplicando  MVT (Modelo - Vista - Template). El objetivo principal fue incorporar funcionalidades básicas y avanzadas para construir una aplicación web robusta, moderna y personalizable.

---

## Funcionalidades implementadas

1. Herencia de HTML 
   Todos los templates comparten una base (`base.html`) que incluye la estructura común del sitio: header, footer, navegación y uso de bloques `{% block %}` para contenido dinámico.

2. Modelos   
   En la app `blog`, se definieron los siguientes modelos:
   - `Post`: título, contenido, autor, fecha.
   - `Categoria`: nombre, descripción.
   - `Comentario`: post relacionado, autor, contenido, fecha.

3. Formularios para insertar datos  
   Se crearon formularios (`forms.py`) para insertar:
   - Nuevos posts.
   - Categorías.
   - Comentarios.

4. Formulario de búsqueda  
   Se implementó un formulario de búsqueda por título dentro del blog. La vista filtra y devuelve resultados relacionados con el término ingresado.

5. Manejo de errores - Página 404  
   Se añadió una vista personalizada para mostrar un template amigable cuando una página no es encontrada.

6. Sistema de usuarios completo
   - Registro de nuevos usuarios.
   - Ingreso (login) y cierre de sesión (logout).
   - Edición del perfil de usuario.

7. Restricción de contenido por sesión
   Se restringió el acceso a ciertas vistas del blog a usuarios registrados (por ejemplo, agregar posts, comentarios o editar).

---
## Tecnologías usadas

- Python 3.x
- Django 4.x
- Visual Studio Code
- HTML5 / CSS3
- Bootstrap (opcional)
- SQLite (base de datos por defecto)

## Tecnologías y librerías a incorporar (en próxima etapa)

Se planificó modernizar la interfaz y extender las funcionalidades:
- **Tailwind CSS** y **Astro** para diseño moderno y responsivo.
- **React**, **Framer Motion**, **Lucide Icons** para animaciones y UI dinámico.
- **Modo claro/oscuro** y tema personalizable.
- **Pagefind** para mejorar el sistema de búsqueda.
- **Markdown extendido**, tabla de contenido y fuente RSS.

---

## ¿Cómo probar el proyecto?

- Asegúrate de tener Python y Django instalados previamente.  

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/Daljulian/Entrega_final_Dalessandro.git
   cd Entrega_final_Dalessandro
2. Crear un entorno virtual
    ```bash
python -m venv env
source env/bin/activate     # En Mac/Linux
env\Scripts\activate.bat    # En Windows

3. Instalar dependencias
    pip install -r requirements.txt

4. Crear y migrar la base de datos
    python manage.py makemigrations
    python manage.py migrate

## Ejecución

Para correr el servidor localmente:

```bash
python manage.py runserver
Entrar en el navegador a: http://127.0.0.1:8000/


 Cómo probar cada funcionalidad...

1. **Herencia de HTML:**  
   - Ir a `/`, verás el `base.html` aplicado a todas las páginas.

2. **Modelos y formularios:**  
   - Ir a `/blog/nuevo/` para crear una nueva entrada.
   - Ir a `/autores/nuevo/` o `/categorias/nuevo/` para cargar esos modelos.

3. **Búsqueda:**  
   - Usar el formulario de búsqueda en la barra superior.

4. **Manejo de error 404:**  
   - Visitar una URL inexistente como `/paginax/`.

5. **Registro/Login/Logout:**  
   - Ir a `/users/register/` para registrarse.
   - `/users/login/` para iniciar sesión.
   - `/users/logout/` para cerrar sesión.

6. **Edición de usuario:**  
   - Ingresar al perfil luego de iniciar sesión y hacer clic en "Editar perfil".

7. **Restricción de vistas:**  
   - Cerrar sesión y probar acceder a `/blog/nuevo/` para comprobar que está restringido.


## Autor

Julián D'Alessandro Magrini  
Proyecto académico - Curso Python 2025