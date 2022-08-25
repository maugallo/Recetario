# RECETARIO - MAIN:
"""
Código encargado de elaborar la interfaz gráfica para el usuario, utilizando
como herramienta Tkinter. Se elabora el diseño visual y la funcionalidad de
cada uno de los botones, complementándose con el archivo "backend.py".
"""

import tkinter as tk
from tkinter import FLAT, TOP, LEFT, RIGHT, END, StringVar, Tk
from tkinter.messagebox import showinfo, showerror
from PIL import ImageTk, Image
import backend

# Clases:
class PanelSuperior(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=3, relief=FLAT, bg="#ffffd5")
        self.pack(side=TOP)
        # Label:
        self.label = tk.Label(
            self,
            text="RECETARIO",
            font=("Courier", 49, "bold"),
            fg="#FEFFFF",
            bg="#D7AA68",
            width=26,
        )
        self.label.pack(padx=20, pady=4, ipady=10)


class PanelIzq(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(relief=FLAT, bg="#ffffd5")
        self.pack(side=LEFT)
        # Buttons:
        for opcion in botones_menu:
            self.opcion = tk.Button(
                self,
                font=("Courier", 18, "bold"),
                text=opcion.title(),
                fg="#FEFFFF",
                bg="#D7AA68",
                width=35,
                height=2,
                relief=FLAT,
            )
            self.opcion.pack(padx=20, pady=4)
            botones_guardados.append(self.opcion)
        # Funciones de cada button:
        botones_guardados[0].config(command=mostrar_categorias_leer)
        botones_guardados[1].config(command=mostrar_categorias_crear)
        botones_guardados[2].config(command=crear_categoria)
        botones_guardados[3].config(command=cat_eliminar_recetas)
        botones_guardados[4].config(command=mostrar_categorias_eliminar)
        botones_guardados[5].config(command=app.quit)


class PanelDer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        self.pack(side=RIGHT)
        # Imagen:
        self.img = Image.open("imagen.jpg")
        self.img = self.img.resize((400, 400))
        self.img = ImageTk.PhotoImage(self.img)
        # Labels:
        self.label = tk.Label(
            self,
            text=contar_recetas(),
            font=("Courier", 20, "bold"),
            fg="#FEFFFF",
            bg="#D7AA68",
            width=27,
        )
        self.label.pack(padx=20, ipady=5)

        self.label2 = tk.Label(self, image=self.img)
        self.label2.pack(pady=15)


class Categorias(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Label:
        self.label = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Categorías:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=35,
            height=2,
            relief=FLAT,
        )
        self.label.pack(pady=4, padx=20)

    # Buttons para opción leer receta:
    def agregar_botones_lectura(self):
        categorias = backend.ver_categorias()
        if len(categorias) == 0:
            showerror("Error", "¡No hay categorías disponibles!")
            reset()
        else:
            for cat in categorias:
                cat = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=cat.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda x=cat: mostrar_recetas(x),
                )
                cat.pack(pady=4, padx=20)
                botones_categorias.append(cat)
            self.pack(side=RIGHT)

    # Buttons para opción crear receta:
    def agregar_botones_crear(self):
        categorias = backend.ver_categorias()
        if len(categorias) == 0:
            showerror("Error", "¡No hay categorías disponibles!")
            reset()
        else:
            for cat in categorias:
                cat = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=cat.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda x=cat: crear_receta(x),
                )
                cat.pack(pady=4, padx=20)
                botones_categorias.append(cat)
            self.pack(side=RIGHT)

    # Buttons para opción eliminar receta:
    def agregar_botones_eliminar(self):
        categorias = backend.ver_categorias()
        if len(categorias) == 0:
            showerror("Error", "¡No hay categorías disponibles!")
            reset()
        else:
            for cat in categorias:
                cat = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=cat.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda x=cat: mostrar_recetas_eliminar(x),
                )
                cat.pack(pady=4, padx=20)
                botones_categorias.append(cat)
            self.pack(side=RIGHT)

    # Eliminar todos los buttons:
    def eliminar_botones(self):
        for button in botones_categorias:
            button.destroy()


class Recetas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Label:
        self.label = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Recetas:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=35,
            height=2,
            relief=FLAT,
        )
        self.label.pack(pady=4, padx=20)

    # Buttons del frame:
    def agregar_botones(self, categoria_elegida):
        recetas = backend.ver_recetas(categoria_elegida)
        if recetas == 0:
            showerror("Error", "¡No hay recetas disponibles!")
            reset()
        else:
            for rec in recetas:
                rec = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=rec.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda y=rec: leer_receta(y),
                )
                rec.pack(pady=4, padx=20)
                botones_recetas.append(rec)
            self.pack(side=RIGHT)

    # Eliminar todos los buttons:
    def eliminar_botones(self):
        for button in botones_recetas:
            button.destroy()


class VisorReceta(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Button volver:
        self.volver = tk.Button(
            self,
            font=("Courier", 18, "bold"),
            text="Volver",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=35,
            height=2,
            relief=FLAT,
            command=reset,
        )
        self.volver.pack(pady=4, padx=20)
        # Visor del frame:
        self.visor = tk.Text(
            self,
            font=("Courier", 16, "bold"),
            relief=FLAT,
            highlightthickness=2,
            highlightcolor="dark gray",
        )
        self.visor.pack(pady=4, padx=20)

    # Colocar la información del archivo en el visor:
    def llenar_visor(self):
        info = backend.leer_receta(receta_elegida, categoria_elegida)
        self.visor.insert(END, info)

    # Vaciar el visor:
    def vaciar_visor(self):
        self.visor.delete(0.0, END)


class CrearReceta(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Button para crear:
        self.crear = tk.Button(
            self,
            font=("Courier", 18, "bold"),
            text="Crear",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=32,
            height=1,
            relief=FLAT,
            command=lambda: self.aviso_crear(
                self.entry.get(), self.text.get(0.0, END), categoria_elegida
            ),
        )
        self.crear.pack(ipady=0.5)
        # Label del nombre:
        self.nombre = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Nombre:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=32,
            height=0,
            relief=FLAT,
        )
        self.nombre.pack(pady=4)
        # Entry del nombre:
        self.variablenombre = StringVar()
        self.entry = tk.Entry(
            self,
            font=("Courier", 16, "bold"),
            textvariable=self.variablenombre,
            width=33,
            relief=FLAT,
            highlightthickness=2,
            highlightcolor="dark gray",
        )
        self.entry.pack()
        # Label de la descripción:
        self.contenido = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Contenido:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=32,
            height=0,
            relief=FLAT,
        )
        self.contenido.pack(pady=2)
        # Text del contenido:
        self.text = tk.Text(
            self,
            font=("Courier", 16, "bold"),
            relief=FLAT,
            highlightthickness=2,
            highlightcolor="dark gray",
        )
        self.text.pack(padx=20)

    # Vaciar nombre y contenido:
    def vaciar(self):
        self.entry.delete(first=0, last=END)
        self.text.delete(0.0, END)

    def aviso_crear(self, nombre, contenido, categoria_elegida):
        if len(nombre) == 0 or len(contenido) == 1:
            showerror("Error", "Error al crear la receta\n¡Hay campos vacíos!")
        else:
            backend.crear_receta(nombre, contenido, categoria_elegida)
            frame3.label.config(text=contar_recetas())
            showinfo("", "¡Receta creada con éxito!")
        reset()


class CrearCategoria(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Label del nombre:
        self.nombre = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Nombre:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=25,
            height=0,
            relief=FLAT,
        )
        self.nombre.pack(padx=20, pady=4)
        # Entry del nombre:
        self.variablenombre = StringVar()
        self.entry = tk.Entry(
            self,
            font=("Courier", 16, "bold"),
            textvariable=self.variablenombre,
            width=30,
            relief=FLAT,
            highlightthickness=2,
            highlightcolor="dark gray",
        )
        self.entry.pack(padx=30)
        # Imagen:
        self.img = Image.open("imagen.jpg")
        self.img = self.img.resize((350, 350))
        self.img = ImageTk.PhotoImage(self.img)
        self.label2 = tk.Label(self, image=self.img)
        self.label2.pack(pady=10)
        # Button:
        self.crear = tk.Button(
            self,
            font=("Courier", 18, "bold"),
            text="Crear",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=32,
            height=1,
            relief=FLAT,
            command=lambda: self.aviso_crear(self.entry.get()),
        )
        self.crear.pack(padx=20)

    # Vaciar nombre:
    def vaciar(self):
        self.entry.delete(first=0, last=END)

    def aviso_crear(self, nombre):
        if len(nombre) == 0:
            showerror("Error", "Error al crear la categoría\n¡Hay campos vacíos!")
        else:
            backend.crear_categoria(nombre)
            showinfo("", "¡Categoría creada con éxito!")
        reset()


class EliminarReceta(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")

    # Agregar buttons:
    def agregar_botones(self, categoria_elegida):
        recetas = backend.ver_recetas(categoria_elegida)
        if recetas == 0:
            showerror("Error", "¡No hay recetas disponibles!")
            reset()
            cat_eliminar_recetas()
        else:
            for rec in recetas:
                rec = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=rec.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda y=rec: self.aviso_eliminar(y, categoria_elegida),
                )
                rec.pack(pady=4, padx=20)
                botones_recetas.append(rec)

    def aviso_eliminar(self, nombre, categoria_elegida):
        backend.eliminar_receta(nombre, categoria_elegida)
        showinfo("", "Receta eliminada con éxito!")
        frame3.label.config(text=contar_recetas())
        reset()


class EliminarCategoria(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#ffffd5")
        # Label:
        self.label = tk.Label(
            self,
            font=("Courier", 18, "bold"),
            text="Categorías:",
            fg="#FEFFFF",
            bg="#D7AA68",
            width=35,
            height=2,
            relief=FLAT,
        )
        self.label.pack(pady=4, padx=20)

    # Agregar buttons:
    def agregar_botones(self):
        # Buttons del frame para eliminar:
        categorias = backend.ver_categorias()
        if len(categorias) == 0:
            showerror("Error", "¡No hay categorías disponibles!")
            reset()
        else:
            for cat in categorias:
                cat = tk.Button(
                    self,
                    font=("Courier", 18, "bold"),
                    text=cat.capitalize().title(),
                    fg="#FEFFFF",
                    bg="#D7AA68",
                    width=30,
                    height=0,
                    relief=FLAT,
                    command=lambda x=cat: eliminar_categoria(x),
                )
                cat.pack(pady=4, padx=20)
                botones_categorias.append(cat)
            self.pack(side=RIGHT)

    # Eliminar todos los buttons:
    def eliminar_botones(self):
        botones_categorias.clear()


# Funciones:
def config_basica():
    app.geometry("1020x630")
    app.resizable(0, 0)
    app.title("Recetario")
    app.config(bg="#ffffd5")
    app.iconphoto(True, tk.PhotoImage(file="icon.png"))


def contar_recetas():
    cantidad = backend.contar_recetas()
    return f"Recetas Totales: {cantidad}"


def reset():
    for frame in lista_frames:
        frame.pack_forget()
    frame_categorias.eliminar_botones()
    frame_recetas.eliminar_botones()
    frame_visor.vaciar_visor()
    frame_crear_receta.vaciar()
    frame_crear_categoria.vaciar()
    frame_eliminar_categoria.eliminar_botones()
    frame3.pack(side=RIGHT)


# Opción 1 "Leer Recetas":
def mostrar_categorias_leer():
    frame3.pack_forget()
    frame_categorias.eliminar_botones()
    frame_categorias.agregar_botones_lectura()


def mostrar_recetas(x):
    global categoria_elegida
    categoria_elegida = x
    frame_categorias.pack_forget()
    frame_recetas.agregar_botones(categoria_elegida)


def leer_receta(y):
    global receta_elegida
    receta_elegida = y
    frame_recetas.pack_forget()
    frame_visor.llenar_visor()
    frame_visor.pack(side=RIGHT)


# Opción 2 "Crear Receta":
def mostrar_categorias_crear():
    frame3.pack_forget()
    frame_categorias.eliminar_botones()
    frame_categorias.agregar_botones_crear()


def crear_receta(x):
    global categoria_elegida
    categoria_elegida = x
    frame_categorias.pack_forget()
    frame_crear_receta.pack(side=RIGHT)


# Opción 3 "Crear Categoría":
def crear_categoria():
    frame3.pack_forget()
    frame_crear_categoria.pack(side=RIGHT)


# Opción 4 "Eliminar Receta":
def cat_eliminar_recetas():
    frame3.pack_forget()
    frame_categorias.eliminar_botones()
    frame_categorias.agregar_botones_eliminar()


def mostrar_recetas_eliminar(z):
    global categoria_elegida
    categoria_elegida = z
    frame_categorias.pack_forget()
    frame_eliminar_receta.agregar_botones(categoria_elegida)
    frame_eliminar_receta.pack(side=RIGHT)


# Opción 5 "Eliminar Categoría":
def mostrar_categorias_eliminar():
    frame3.pack_forget()
    frame_eliminar_categoria.agregar_botones()


def eliminar_categoria(x):
    categoria_elegida = x
    backend.eliminar_categoria(categoria_elegida)
    showinfo("", "¡Categoría eliminada con éxito!")
    frame3.label.config(text=contar_recetas())
    reset()


# Variables:
botones_menu = [
    "Leer Receta",
    "Crear Receta",
    "Crear Categoría",
    "Eliminar Receta",
    "Eliminar Categoría",
    "Cerrar Recetario",
]

botones_guardados = []

botones_categorias = []

botones_recetas = []

lista_frames = []

# Crear ventana:
app = Tk()

# Main:
backend.verificar_ruta()
config_basica()
frame1 = PanelSuperior(app)
frame2 = PanelIzq(app)
frame3 = PanelDer(app)
lista_frames.append(frame3)
frame_categorias = Categorias(app)
lista_frames.append(frame_categorias)
frame_recetas = Recetas(app)
lista_frames.append(frame_recetas)
frame_visor = VisorReceta(app)
lista_frames.append(frame_visor)
frame_crear_receta = CrearReceta(app)
lista_frames.append(frame_crear_receta)
frame_crear_categoria = CrearCategoria(app)
lista_frames.append(frame_crear_categoria)
frame_eliminar_receta = EliminarReceta(app)
lista_frames.append(frame_eliminar_receta)
frame_eliminar_categoria = EliminarCategoria(app)
lista_frames.append(frame_eliminar_categoria)

# Mantener abierta la ventana:
app.mainloop()
