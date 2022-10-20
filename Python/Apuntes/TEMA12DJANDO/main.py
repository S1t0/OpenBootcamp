#para iniciar un proyecto en django ponemos
# django-admin startproject nombredelproyecto .
# podemos iniciar un servidor con el comando python3 manage.py runserver
#asi pdemos ir viendo los cambios que vamos haciendo en la web
#en djando se va creando el proyecto por aplicaciones, no todo en el proyecto, y 
#luego cada aplicacion hace una cosa, al final todo va en concordancia
#Para crear una aplicacion ejecuatamos python3 manage.py startapp nombredelaaplicacion(en nuestro ejemplo le hemos puesto catalog)
#Para conectar mi aplicacion con el proyecto general nos vamos a settings y en el apartado INSTALLED_APPS, añadimos catalog.apps.CatalogConfig
#ademas en el apartado ursls hay que poner path(catalog/,include(catalog.urls)) e importar en el documento el include,
#tambien creamos dentro de la carpeta catalog un fichero llamado urls.py y poner lo que hay puesto dentro del documento.
#ahora seguimos en la carpeta principal del proyecto ponemos python3 manage.py makemigrations y luego python3 manage.py migrate
#En django podemos tener un superusuario, en localhost:8000/admin/ nos podemos meter con usuario y contraseña, para crear ese 
#usuario y contraseña ponemos python3 manage.py createsuperuser, admin el usuario, y adming la contraseña les e puesto
#Dentro de la administracion de django podemos ver la base de datos, aqui nos creamos los modelos de datos, se crean en el archivo
#models dentro de nuestra aplicacion catalog, una vez modificacmos el models, en la terminal ponemos python3 manage.py makemigrations y luego 
#lo mismo pero con migrate
#Cuando creamos los modelos los importamos en el archivo admin.py


