# Nombre: Hector Rafael Nivar Gomez
# Matricula: 1-25-9465

from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from clientes import Clientes
from pedidos import Pedidos
from prooveedor import Proveedor
from informacion import Informacion
import os
import sys


class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frame = {}
        self.buttons = []
        for i in (Ventas, Inventario, Clientes, Pedidos, Proveedor, Informacion):
            frame = i(self)
            self.frame[i] = frame
            frame.pack()
            frame.configure(
                bg='lightblue', highlightbackground='gray', highlightthickness=1)
            frame.place(x=0, y=40, width=1100, height=600)
        self.show_frame(Ventas)

    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()

    def ventas(self):
        self.show_frame(Ventas)

    def inventario(self):
        self.show_frame(Inventario)

    def clientes(self):
        self.show_frame(Clientes)

    def pedidos(self):
        self.show_frame(Pedidos)

    def proveedor(self):
        self.show_frame(Proveedor)

    def informacion(self):
        self.show_frame(Informacion)

    def widgets(self):
        frame2 = tk.Frame(self)
        frame2.place(x=0, y=0, width=1100, height=40)

        self.btn_ventas = Button(
            frame2, fg='black', text='Ventas', font='sans 16 bold', command=self.ventas)
        # 1100/6 es el ancho de cada boton, ya que hay 6 botones en total, este me parecio un metodo mas rapido que sumar cada vez.
        self.btn_ventas.place(x=0, y=0, width=1100/6, height=40)

        self.btn_inventario = Button(
            frame2, fg='black', text='Inventario', font='sans 16 bold', command=self.inventario)
        self.btn_inventario.place(x=1100/6, y=0, width=1100/6, height=40)

        self.btn_clientes = Button(
            frame2, fg='black', text='Clientes', font='sans 16 bold', command=self.clientes)
        # la multiplicacion la uso para poner los botones en su lugar.
        self.btn_clientes.place(x=1100/6*2, y=0, width=1100/6, height=40)

        self.btn_pedidos = Button(
            frame2, fg='black', text='Pedidos', font='sans 16 bold', command=self.pedidos)
        self.btn_pedidos.place(x=1100/6*3, y=0, width=1100/6, height=40)

        self.btn_proveedor = Button(
            frame2, fg='black', text='Proveedores', font='sans 16 bold', command=self.proveedor)
        self.btn_proveedor.place(x=1100/6*4, y=0, width=1100/6, height=40)

        self.btn_informacion = Button(
            frame2, fg='black', text='Información', font='sans 16 bold  ', command=self.informacion)
        self.btn_informacion.place(x=1100/6*5, y=0, width=1100/6, height=40)

        self.buttons = [self.btn_ventas, self.btn_inventario, self.btn_clientes,
                        self.btn_pedidos, self.btn_proveedor, self.btn_informacion]
