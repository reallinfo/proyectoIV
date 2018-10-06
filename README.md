# AleatoriedAPP
## Aplicación para el proyecto de Infraestructura Virtual

### Introducción
AleatoriedAPP es una aplicación desarrollada en Django 2.0.2 usando Python 3 para el backend y una sola template para la interacción con el usuario.

La template está renderizada por Django pero, haciendo uso de *{% verbatim %}*, se consigue que se renderice sólo una vez y, a partir de ahí, se manipulada exclusivamente por un controlador escrito en AngularJS.

El código CSS es principalmente usado a través de bootstrap, excepto para algunas cosas concretas.

El objetivo final de la aplicación es generar datos aleatorios en diferentes formatos y, en un último paso, almacenar las entradas de los usuarios y mostrarlas aleatoriamente a otros bajo petición.

En lo que respecta a la asignatura, además de todo el desarrollo de la aplicación y su despliegue, se trata de hacer una aplicación con una buena diferenciación entre back y front end y que haga uso de varias tecnologías. Concretamente, Django sólo espera las peticiones del frontend manipulado por Angular y almacena lo que corresponda en la base de datos.
