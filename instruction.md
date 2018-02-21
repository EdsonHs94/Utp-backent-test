# Technical Test Backend

## Objetivo 
La prueba consistirá en crear un simple API REST para un único recurso, la prueba se dividirá en 2 funcionalidades basicas y 3 funcionalidades adicionales (opcionales) 

Se evaluara: 

* Evaluar el conocimiento sobre la creacion de un API REST
* Comprobar el conocimiento independientemente de la herramienta / framework que se utilice.
* Evaluar buenas prácticas en el código.
* Evaluar el modelo mental que se tiene para la organización de clases, funciones, módulos.


## Instrucciones

Algunas instrucciones a tener en cuenta:

- Para enviar la prueba se clonará este repositorio y se harán commits en la rama `master`.
- Elegir el lenguaje y el framework de su preferencia.
- Elegir la BD de su preferencia 
- Elegir los servicios adicionales de su preferencia.
- **Tiempo máximo:** 2 horas 

## 1. Funcionalidades basicas

**Usuario y Autentificación**

Se desea que el API sea restringido mediante algún método de autenticación basica.

**Endpoints para Notas**

Se desea crear endpoints para poder administrar **notas** (crear y listar), los datos se guardará en una base de datos 

**Nota:** Los campos usados en la BD son irrelevantes y son propuestos por el evaluado

## 2. Funcionalidades adicionales

Las siguientes funcionalidades se construirán sobre la funcionalidad base.

**Serialización y validación**

Se desea validar los datos que se reciben via POST y mostrar los errores al usuario que usa el API, serializar la lista de objetos para enviarlas como json (los criterios de validacion son propuestos por el evaluado)


**Autorización**

Se desea asociar una **nota** con un **usuario**, de tal manera que cada usuario solo pueda ver sus propias notas.


**JWT**

Se desea que el usuario se autentifique mediante json web tokens.