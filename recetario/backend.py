# RECETARIO - BACKEND:
"""
Código encargado de la parte interna del programa. Formado por funciones que
manipulan tanto las carpetas como los archivos al igual que definir la ruta de estos.
Se utilizan los módulos Pathlib y OS.
"""

from pathlib import Path
import os

ruta = os.getcwd() + "\\recetas"

"""Verificar si la carpeta donde se almacenarán los archivos existe, en caso de no
existir se crea automáticamente."""


def verificar_ruta():
    respuesta = os.path.exists(ruta)
    if respuesta == True:
        print("Existe")
    else:
        os.makedirs(ruta)


def contar_recetas():
    cantidad = 0
    for archivo in Path(ruta).glob("**/*.txt"):
        cantidad += 1
    return cantidad


def ver_categorias():
    categorias = []
    direccion = Path(ruta)
    for carpeta in direccion.iterdir():
        categorias.append(carpeta.stem)
    return categorias


def ver_recetas(categoria):
    recetas = []
    for archivos in Path(ruta + "\\" + categoria).glob("*.txt"):
        recetas.append(archivos.stem)
    if len(recetas) == 0:
        return 0
    else:
        return recetas


def leer_receta(receta, categoria):
    direccion = Path(ruta + "\\" + categoria)
    os.chdir(direccion)
    try:
        archivo = open(receta + ".txt", "r")
    except FileNotFoundError:
        info = "[Archivo vacío]"
        return info
    else:
        info = archivo.read()
        archivo.close()
        return info


def crear_receta(receta, contenido, categoria):
    direccion = Path(ruta + "\\" + categoria)
    os.chdir(direccion)
    Path(receta + ".txt").touch()
    archivo = open(receta + ".txt", "w")
    archivo.write(contenido)
    archivo.close()


def crear_categoria(categoria):
    categoria = categoria.capitalize()
    direccion = Path(ruta + "\\" + categoria)
    os.makedirs(direccion)


def eliminar_receta(receta, categoria):
    direccion = Path(ruta + "\\" + categoria)
    os.chdir(direccion)
    Path(receta + ".txt").unlink()


def eliminar_categoria(categoria):
    direccion = Path(ruta + "\\" + categoria)
    os.chdir(direccion)
    for archivos in Path(direccion).glob("*.txt"):
        Path(archivos.name).unlink()
    os.chdir(direccion.parent)
    os.rmdir(direccion)
