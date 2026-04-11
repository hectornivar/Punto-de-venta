# Nombre: Hector Rafael Nivar Gomez
# Matricula: 1-25-9465
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from container import Container
from PIL import Image, ImageTk


class Login(tk.Frame):
    db_name = 'database.db'

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def login(self):
        user = self.username.get()
        pas = self.password.get()

        if self.validacion(user, pas):
            consulta = 'SELECT * FROM usuarios WHERE username = ? AND password = ?'
            parametros = (user, pas)

            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchall()

                    if result:
                        self.control1()
                    else:
                        self.username.delete(0, 'end')
                        self.password.delete(0, 'end')
                        messagebox.showerror(
                            'Error', 'Usuario o contraseña incorrectos')
            except sqlite3.Error as e:
                messagebox.showerror(
                    title='Error', message=f'No se conectó a la base de datos: {e}')
        else:
            messagebox.showerror(
                title='Error', message='Llene todas las casillas')

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Registro)

    def widgets(self):
        fondo = tk.Frame(self, bg='lightblue')
        fondo.place(x=0, y=0, width=1100, height=650)

        self.bg_image = Image.open(
            'G:/Mi unidad/Universidad/Python/Programacion2_POO/Punto_de_venta/imagenes/fondo.png')
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(fondo, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self, bg='white',
                          highlightbackground='black', highlightthickness=1)
        frame1.place(x=350, y=70, width=400, height=650)

        self.logo_image = Image.open(
            'G:/Mi unidad/Universidad/Python/Programacion2_POO/Punto_de_venta/imagenes/logo.png')
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(
            frame1, image=self.logo_photo, background='white')
        self.logo_label.place(x=100, y=20)

        user = ttk.Label(frame1, text='Nombre de usuario',
                         font='arial 16 bold', background='white')
        user.place(x=110, y=250)
        self.username = ttk.Entry(frame1, font='arial 16 bold')
        self.username.place(x=80, y=280, width=240, height=40)

        pas = ttk.Label(frame1, text='Contraseña',
                        font='arial 16 bold', background='white')
        pas.place(x=140, y=320)
        self.password = ttk.Entry(frame1, font='arial 16 bold', show='*')
        self.password.place(x=80, y=350, width=240, height=40)

        btn1 = ttk.Button(frame1, text='Iniciar sesión', command=self.login)
        btn1.place(x=80, y=420, width=240, height=40)

        btn2 = ttk.Button(frame1, text='Registrarse', command=self.control2)
        btn2.place(x=80, y=480, width=240, height=40)


class Registro(tk.Frame):
    db_name = 'database.db'

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def eje_consulta(self, consulta, parametros=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror(
                title='Error', message=f'Error al ejecutar la consulta: {e}')

    def registro(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()
        if self.validacion(user, pas):
            if len(pas) < 6:
                messagebox.showerror(
                    title='Error', message='Contraseña demasiodo corta, debe tener al menos 6 caracteres')
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
            else:
                if key == '1234':
                    consulta = 'INSERT INTO usuarios VALUES (?, ?, ?)'
                    parametros = (None, user, pas)
                    self.eje_consulta(consulta, parametros)
                    self.control1()
                else:
                    messagebox.showerror(
                        title='Registro', message='Error al ingresar el codigo de registro')
        else:
            messagebox.showerror(title='Error', message='Llene sus datos')

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Login)

    def widgets(self):

        fondo = tk.Frame(self, bg='lightblue')
        fondo.place(x=0, y=0, width=1100, height=650)

        self.bg_image = Image.open(
            'G:/Mi unidad/Universidad/Python/Programacion2_POO/Punto_de_venta/imagenes/fondo.png')
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(fondo, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self, bg='white',
                          highlightbackground='black', highlightthickness=1)
        frame1.place(x=350, y=10, width=400, height=650)

        self.logo_image = Image.open(
            'G:/Mi unidad/Universidad/Python/Programacion2_POO/Punto_de_venta/imagenes/logo.png')
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(
            frame1, image=self.logo_photo, background='white')
        self.logo_label.place(x=100, y=20)

        user = ttk.Label(frame1, text='Nombre de usuario',
                         font='arial 16 bold', background='white')
        user.place(x=110, y=250)
        self.username = ttk.Entry(frame1, font='arial 16 bold')
        self.username.place(x=80, y=280, width=240, height=40)

        key = ttk.Label(frame1, text='Codigo de registro',
                        font='arial 16 bold', background='white')
        key.place(x=100, y=420)
        self.key = ttk.Entry(frame1, font='arial 16 bold')
        self.key.place(x=80, y=470, width=240, height=40)

        pas = ttk.Label(frame1, text='Contraseña',
                        font='arial 16 bold', background='white')
        pas.place(x=140, y=320)
        self.password = ttk.Entry(frame1, font='arial 16 bold', show='*')
        self.password.place(x=80, y=350, width=240, height=40)

        btn3 = ttk.Button(frame1, text='Registrarse', command=self.registro)
        btn3.place(x=80, y=520, width=240, height=40)

        btn4 = ttk.Button(frame1, text='Regresar', command=self.control2)
        btn4.place(x=80, y=570, width=240, height=40)
