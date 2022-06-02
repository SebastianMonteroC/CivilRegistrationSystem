#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM

from tkinter import *
import tkinter as tk
import html
import pickle
import TP3_Pag_Princ

def inicializarArbol(): 
    global listaPersonas
    try:
        archivo = open("RegistroNacimientos.txt","rb")
        listaPersonas = pickle.load(archivo)
        archivo.close()
        ventanaArbol()
    except:
        archivo = open("RegistroNacimientos.txt","wb")
        archivo.close()
        ventanaArbol()

def funcionRegresar():
    TP3_Pag_Princ.paginaPrincipal()
    arbolWindow.destroy()
    
def ventanaArbol():
    global listaNombres
    listaNombres = []
    global arbolWindow
    arbolWindow = Tk()
    arbolWindow.resizable(0,0)
    arbolWindow.title("Árbol genealógico")
    arbolWindow.geometry("530x400")

    Label(arbolWindow,text="Mostrar Árbol Genealógico",fg="black",font="none 14").place(x = 155,y = 15)
    Label(arbolWindow,text="Persona: ",fg="black",font="none 10").place(x=20,y=55)
    Label(arbolWindow,text="Resultado de la búsqueda: ",fg="black",font="none 10").place(x=20,y=155)
    
    for i in range(0, len(listaPersonas)):
        nombre = listaPersonas[i][3] + " " + listaPersonas[i][4]
        listaNombres.append(nombre)
    
    global variableNom
    variableNom = StringVar(arbolWindow)
    OptionMenu(arbolWindow, variableNom, *listaNombres).place(x = 100, y = 55)

    Button(arbolWindow, text = "Mostrar", fg = "black", font = "none 10", height = 2, width = 15, command = mostrarArbol).place(x = 100, y = 100)
    Button(arbolWindow, text  = "Limpiar", fg = "black", font = "none 10", height = 2, width = 15, command = limpiarArbol).place(x = 240, y = 100)
    Button(arbolWindow, text  = "Regresar", fg = "black", font = "none 10", height = 2, width = 15, command = funcionRegresar).place(x = 380, y = 100)

def mostrarArbol():
    for i in range(0, len(listaNombres)):
        if variableNom.get() == listaNombres[i]:
            textoMadre = listaPersonas[i][14]
            textoPadre = listaPersonas[i][12]
            textoHijo = listaPersonas[i][3]
            Label(arbolWindow,text=textoMadre,fg="black",font="none 10").place(x=120,y=205)
            Label(arbolWindow,text=textoPadre,fg="black",font="none 10").place(x=350,y=205)
            Label(arbolWindow,text=textoHijo,fg="black",font="none 10").place(x=220,y=315)
            break
        else:
            continue


    
def limpiarArbol():
    variableNom.set("   ")
    
