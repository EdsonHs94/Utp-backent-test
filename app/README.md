# Prueba Notas

Para realizar esta aplicacion se utilizaron las siguientes tecnologias (python).

  - Fhalcon como framework
  - Gunicorn como servidor

# Comentarios

  - Para esta aplicacion solo e usado el api de Flacon, queriendo asemejar al enfoque DDD (Diseño guiado por el dominio)
  - Por el tiempo no pude incluirle a este desarrollo un contenedor de docker
  - Por tiempo algunos archivos no estan ordenados del todo
  - Por tiempo no inclui algun tipo de migracion para crear las tablas
  - Por falta de tiempo el metodo de autorizacion es demasiado basico y simple
  - El framework  que e usado es poco conocido y nada intrusivo por lo tanto la estructura y modulos son de mi autoria, el framework no me apoyado con la creacion de ninguna carpeta
  - E trabajado con jwt y con validaciones pero por falta de tiempo no e podido incluir ninguno ya que la creacion de la estructura de tomo demasiado tiempo
  - PD: para que el request sea exitoso la cabecera del api debe ser Authorization: validToken "simulando" asi el uso de JWT
  - PD2: Al no agregarle migraciones se debe crear una tabla "notes": campos id->Autoin message,name,author y una bd "db_notes"
  
### Instalacion

Antes de hacer funcionar este servicio hay que aclarar que los pasos de instalacion estan vistos para el uso de python3 y pip3

Primero crearemos un venv
```sh
$ python3 -m venv api-env
```

Luego activamos este venv
```sh
$ source api-env/bin/activate 
```

Luego instalamos las dependencias
```sh
$ pip3 install -r requeriments.txt
```

Finalmente ponemos a correr la aplicacion
```sh
$ cd app
$ gunicorn wsgi:api
```

Para verificar entrar a localhost:8000

### Uso

Este servicio solo riene 2 rutas que son las siguientes

  - /: ruta base donde da un mensaje simple
  - /notes/{numero}: metodos GET y POST para la creacion y obtencion de notas

