# AleatoriedAPP
## Aplicación para el proyecto de Infraestructura Virtual

### Introducción
AleatoriedAPP es una aplicación desarrollada en Django 2.1.1 usando Python 3 para el backend y una sola template para la interacción con el usuario.

La template está renderizada por Django pero, haciendo uso de *{% verbatim %}*, se consigue que se renderice sólo una vez y, a partir de ahí, se manipulada exclusivamente por un controlador escrito en AngularJS.

El código CSS es principalmente usado a través de bootstrap, excepto para algunas cosas concretas.

El objetivo final de la aplicación es generar datos aleatorios en diferentes formatos y, en un último paso, almacenar las entradas de los usuarios y mostrarlas aleatoriamente a otros bajo petición.

En lo que respecta a la asignatura, además de todo el desarrollo de la aplicación y su despliegue, se trata de hacer una aplicación con una buena diferenciación entre back y front end y que haga uso de varias tecnologías. Concretamente, Django sólo espera las peticiones del frontend manipulado por Angular y almacena lo que corresponda en la base de datos.

### Objetivos
    [X] Crear repositorio y añadir archivo de licencia
    [X] Crear el esqueleto del proyecto Django
    [X] Crear la base de la aplicación que da JSON con datos aleatorios (aleatoriedad)
    [X] Integración de AngularJS para el frontend
    [X] Hacer que aleatoriedad genere números aleatorios
    [X] Crear y cerrar issues con commits
    [ ] Hacer que aleatoriedad genere cadenas aleatorias
    [ ] Conectar la aplicación a una base de datos
    [ ] Almacenar en la base de datos las peticiones de los usuarios
    [ ] Hacer que aleatoriedad muestre a los usuarios las cadenas enviadas por otros
    [ ] Crear tests para el código de Python
    [ ] Depoy a Heroku a través de GitHub
    [ ] Dockerizar la aplicación
