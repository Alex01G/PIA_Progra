import logging
from bs4 import *
import requests
import os
import smtplib
import ssl
from PIL import Image
from PIL.ExifTags import TAGS
from PyPDF2 import PdfFileReader
import os
import socket
import json


def tar_1():
    print("Inicio de la tarea 1")
    logging.info("Se está cargando el archivo de la tarea 1")
    file = "payload.pyw"

    with open("API.json") as f:
        API = json.load(f)

    params = {"apikey": API["key"]}
    filecheck = {"file": (file, open(file, "rb"))}
    response = requests.post("https://www.virustotal.com/vtapi/v2/file/scan", files=filecheck, params=params)
    json_response = response.json()
    logging.info("El escaneo del archivo arrojó los siguientes resultados:")
    print("Resultados del escaneo:")
    print(json_response)

def tar_2():
    logging.info("Inicializando la tarea 2")
    print("\n Preparando tarea 2")
    def folder_create(images):
        try:
            folder_name = "webS_imag"
            os.mkdir(folder_name)
            logging.info("Se creó la carpeta con éxito")

        except:
            logging.info("Ya existe una carpeta con ese nombre")
            folder_create()

        download_images(images, folder_name)
        logging.info("Se están descargando las imágenes")

    def download_images(images, folder_name):
        count = 0
        print(f"{len(images)} imágenes encontradas")
        if len(images) != 0:
            for i, image in enumerate(images):
                try:
                    image_link = image["data-srcset"]
                except:
                    try:
                        image_link = image["data-src"]
                    except:
                        try:
                            image_link = image["data-fallback-src"]
                        except:
                            try:
                                image_link = image["src"]
                            except:
                                pass
                try:
                    r = requests.get(image_link).content
                    try:
                        r = str(r, 'utf-8')

                    except UnicodeDecodeError:
                        with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                            f.write(r)
                        count += 1
                except:
                    pass
            if count == len(images):
                logging.info("Todas las imágenes fueron descargadas exitosamente")
            else:
                print(f"{count} imágenes fueron descargadas de {len(images)}")

    def main(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.findAll('img')
        folder_create(images)

    url = "https://hdqwalls.com/"
    main(url)

def tar_3():
    logging.info("Tarea 3: Inicializando tarea 3")
    print("\n Preparando envío de correo")
    port = 587  
    smtp_server = "smtp.gmail.com"
    data = {}
    with open("pass.json") as f:
        data = json.load(f)
    recibe_email = "adlex010@gmail.com"
    mensaje = """\
    Prueba

    Esta es la prueba de envio de correo del pia de programacion:)."""
    logging.info("Estableciendo valores del envío de correos...")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(data["user"], data["pass"])
        server.sendmail(data["user"], recibe_email, mensaje)
    logging.info("El correo fue enviado exitosamente")
    print("El correo se envió exitosamente")

def tar_4():
    logging.info("Inicializando tarea 4")
    print("\n Iniciando tarea 4")
    ip = socket.gethostbyname(socket.gethostname())
    path = os.getcwd()
    os.system("powershell.exe "+path+"\portscan.ps1 -ip "+ip)
    logging.info("Se terminó la ejecución de la tarea 4")

def tar_5():
    logging.info("Empezando tarea 5")
    print("\n Preparando extracción de metadatos")
    # Cambia de directorio actual al directorio extract_data
    os.chdir("extract_data")

    # Extrae los metadatos de un archivo jpg
    logging.info("Recolecando metadatos del jpg")
    def JpgMeta(target):
        imagen = Image.open(target)
        datos_exif = imagen.getexif()
        jpg_dic = {}
        for tag, value in datos_exif.items():
            etiqueta = TAGS.get(tag, tag)
            valor = datos_exif.get(tag)
            jpg_dic[etiqueta] = valor
        Reporte(jpg_dic, target)

    # Extrae los metadatos de un archivo pdf
    logging.info("Recolectando metadatos del pdf")
    def PdfMeta(target):
        pdf = PdfFileReader(open(target, 'rb'))
        info = pdf.getDocumentInfo()
        pdf_dic = {}
        for i in info:
            pdf_dic[i] = info[i]
        Reporte(pdf_dic, target)

    # Crea el reporte de los datos extraidos en los metadatos
    logging.info("creando reporte")
    def Reporte(dic, target):
        name = target[:-4]+"_reporte.txt"
        f = open(name, 'w')
        for name, valor in dic.items():
            f.write(str(name)+": "+str(valor)+"\n")
        f.close()

    # Llamamos a las funciones
    JpgMeta("imagen.jpg")
    PdfMeta("archivo.pdf")
    print("Extracción de metadatos terminada.\n")
    logging.info("Se ha terminado la tarea 5")