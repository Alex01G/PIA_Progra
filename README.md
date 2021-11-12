Los módulos necesarios y externos a python para la correcta ejecución del código es el sigiente:

beautifulsoup4
bs4
requests
Pillow
PyPDF2

Estos mismos módulos se pueden encontrar en requirements.


Conforme al script está conformado por distintas tareas que funcionan independiente mente de una a la otra, dichas tareas son:
Tarea 1: Filescan
Tarea 2: WebScraping
Tarea 3: Envío de correos
Tarea 4: Escaneo de puertos
Tarea 5: Metadatos

Se tienen 2 scripts con mayor jerarquía.
El Pia_1.py es el encargado de hacer llamar las funciones que están escritas en el Pia_2, donde se almacenan las tareas de seguridad,
esto mediante argparse para ingresar los argumentos a la hora de querer ejecutar el código.


Para poder ejecutarlo hay que especificar el tipo de argumento que se le asignará.
Demostración: 

usage: Pia_1.py [-h] [-filescan] [-dwimg] [-sndmail] [-portscan] [-meta] [-all]

optional arguments:
  -h, --help  show this help message and exit
  -filescan   Escanea el archivo en busca de información del mismo o virus
  -dwimg      Descarga imagenes y crea carpeta donde se alojará
  -sndmail    Envia un correo electronico
  -portscan   Escaneo de puertos
  -meta       Obtiene los metedatos de un .jpg y .pdf
  -all        Se ejecutan todas las tareas
  
  
 Utilidades:
 La primera tarea escaneará un archivo asignado en el código que nos dará información útil del mismo, como a su vez, un link directo a virustotal con el que se evaluará la seguridad del mismo (Necesitará un archivo json para poder ejecutarlo, en él se encuentra el APIKEY de virustotal).
 La segunda tarea se encarga de la descarga de imágenes de un sitio de interés.
 La tercer tarea se basa en el envío de correos, que se utilizará un archivo json para poder acceder a la información de usuario (Habrá que crear uno para cada usuario que 
 requiera usarlo).
 La cuarta se basa en el escaneo de puertos de la red.
 Por último la quinta es la obtención de metadatos de imágenes o archivos previamente colocados en la carpeta extract_data-
