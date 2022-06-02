#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM

import TP3_registrarPersona
import HTML_Final_File
import TP3_arbol
from tkinter import *
import tkinter as tk
import pickle

global listaPersonas

try:
    archivo = open("RegistroNacimientos.txt","rb")
    listaPersonas = pickle.load(archivo)
    archivo.close()
except:
    archivo = open("RegistroNacimientos.txt","wb")
    archivo.close()

def FuncionRegistrar():
    TP3_registrarPersona.ventanaRegistrar()
    window.destroy()

def FuncionArbol():
    TP3_arbol.inicializarArbol()
    window.destroy()
    
def FuncionCertificado():
    HTML_Final_File.inicializarHTML()
    window.destroy()

def FuncionSalir():
    window.destroy()
    quit()


def paginaPrincipal():
    global window
    window = Tk()
    window.title("Tribunal Supremo de Elecciones")
    window.resizable(0,0)
    window.geometry("600x700")

    Label(window, text = "Total de Personas: " + str(len(listaPersonas)), fg = "black", font = "none 8").place(x = 480, y = 5)
    Label(window, text = "Tribunal Supremo de Elecciones", fg = "black", font = "none 18").place(x = 125,y = 20)

    BotonRegistrar = Button(window, text = "Registrar Nacimiento", fg = "black", font = "none 10", height = 4, width = 30, command = FuncionRegistrar).place(x = 175, y = 100)
    
    BotonArbol = Button(window, text = "Mostrar Árbol Genealógico", fg = "black", font = "none 10", height = 4, width = 30, command = FuncionArbol).place(x = 175, y = 250)

    BotonCertificado = Button(window, text = "Certificado de Nacimiento", fg = "black", font = "none 10", height = 4, width = 30, command = FuncionCertificado).place(x = 175, y = 400)

    BotonSalir = Button(window, text = "Salir", fg = "black", font = "none 10", height = 4, width = 30, command = FuncionSalir).place(x = 175, y = 550)

