# Documentación del Curso de Flask

**¿Qué es este repositorio?**

Este repositorio sirve como documentación personal de mi aprendizaje en el curso de Flask. Aquí encontrarás ejemplos de código, proyectos pequeños y apuntes sobre los conceptos clave que he ido adquiriendo a lo largo del curso.

**Contenido:**

* **Ejemplos básicos:** Primeras aplicaciones, rutas, plantillas, formularios, etc.
* **Proyectos:** Aplicaciones más complejas que demuestran la aplicación de los conocimientos adquiridos.
* **Apuntes:** Explicaciones de conceptos clave, resumen de sintaxis y buenas prácticas.

**Tecnologías utilizadas:**

* **Flask:** Microframework de Python para desarrollo web.
* **Otras tecnologías:** HTML, CSS, JavaScript.

**Cómo contribuir:**

Este repositorio es principalmente para mi uso personal, pero si encuentras algún error o tienes alguna sugerencia, no dudes en abrir un issue.

**Agradecimientos:**

Agradezco al creador del curso Lambda Coding por compartir sus conocimientos.

https://www.youtube.com/@lambdacoding9618 

**¡Sigue aprendiendo y construyendo!**

**ANEXOS:**

## Palabras clave:
**Flask:**
* request: Para manejar solicitudes HTTP.
* make_response: Para crear respuestas HTTP personalizadas.
* redirect: Redirigir a otras rutas.
* render_template: Renderizar plantillas HTML.
* session: Almacenar datos específicos del usuario en una sesión.
* Bootstrap: Facilita estilos CSS con Bootstrap.
* FlaskForm, WTForms: Facilitan la creación y validación de formularios HTML.
* DataRequired: Validador que asegura que los campos no estén vacíos.

**Jinja & HTML:**
* {% block %} ... {% endblock %}:
Define secciones que las plantillas hijas pueden sobrescribir o extender.
* super():
Inserta el contenido definido previamente en el bloque correspondiente de una plantilla base o en la misma plantilla.
* url_for:
Genera URLs dinámicas para recursos como rutas o archivos estáticos.
* {% extends "bootstrap/base.html" %}:
Indica que esta plantilla hereda de otra
* Mensajes flash: 
Muestra los mensajes enviados desde el servidor con flash (en Python).
`{% for message in get_flashed_messages() %}
    <div class="alert alert-success">
        {{ message }}
    </div>
{% endfor %}
`
* Macros :
Define una función reutilizable dentro de las plantillas.

