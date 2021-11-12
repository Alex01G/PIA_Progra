from Pia_2 import tar_1, tar_2, tar_3, tar_4, tar_5
import argparse
import sys
import logging

logging.basicConfig(filename='logging',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

parser = argparse.ArgumentParser()
parser.add_argument("-filescan", help="Escanea el archivo en busca de información del mismo o virus", action="store_true")
parser.add_argument(
    "-dwimg", help="Descarga imagenes y crea carpeta donde se alojará", action="store_true")
parser.add_argument("-sndmail", help="Envia un correo electronico", action="store_true")
parser.add_argument("-portscan", help="Escaneo de puertos", action="store_true")
parser.add_argument("-meta", help="Obtiene los metedatos de un .jpg y .pdf", action="store_true")
parser.add_argument("-all", help="Se ejecutan todas las tareas", action="store_true")

args = parser.parse_args()


if __name__ == '__main__':

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.filescan:
        tar_1()

    if args.dwimg:
        tar_2()

    if args.sndmail:
        tar_3()

    if args.portscan:
        tar_4()

    if args.meta:
        tar_5()
    
    if args.all:
        tar_1()
        tar_2()
        tar_3()
        tar_4()
        tar_5()
