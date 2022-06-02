#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from TP3_Pag_Princ import *


def verificarUsuario():
    datosIngresados = []
    usuarioIngresado = usuarioIngresadoEntry.get()
    datosIngresados.append(usuarioIngresado)
    contrasennaIngresada = contrasennaIngresadaEntry.get()
    datosIngresados.append(contrasennaIngresada)
    file = open("usuarioAutorizado.txt", "r")
    linea = file.readlines()
    file.close ()
    datos = '["'+str(datosIngresados)+'"]'
    if datos == str(linea):
        paginaPrincipal()
        ingresarWindow.destroy()
    else:
        messagebox.showwarning("Advertencia","¡Este usuario no posee acceso! \n El usuario o contraseña podrían estar incorrectos")
    
def limpiarEntry():
    contrasennaIngresadaEntry.delete(0,END)
    usuarioIngresadoEntry.delete(0,END)
    
def ventanaIngresar():
    global ingresarWindow
    ingresarWindow = Tk()
    ingresarWindow.resizable(0,0)
    ingresarWindow.title("Ingresar")
    ingresarWindow.geometry("420x300")

    Label(ingresarWindow,text="Digite su usuario y contraseña para ingresar",fg="black",font="none 12").place(x = 20,y = 25)
    Label(ingresarWindow,text="Usuario: ",fg="black",font="none 10").place(x=20,y=75)
    Label(ingresarWindow,text="Contraseña: ",fg="black",font="none 10").place(x=20,y=125)

    valor=""
    global usuarioIngresadoEntry
    usuarioIngresadoEntry = Entry(ingresarWindow, width = 40,textvariable = valor)
    usuarioIngresadoEntry.place(x=125,y=75)

    global contrasennaIngresadaEntry
    contrasennaIngresadaEntry = Entry(ingresarWindow, width = 40,textvariable = valor,show="*")
    contrasennaIngresadaEntry.place(x=125,y=125)

    regist=Button(ingresarWindow,text="Ingresar",command=verificarUsuario,heigh=2,width=40,font="none 12")
    regist.place(x=20,y=160)

    limpiar=Button(ingresarWindow,text="Limpiar",command=limpiarEntry,heigh=2,width=40,font="none 12")
    limpiar.place(x=20,y=220)

    ingresarWindow,mainloop()

usuarioAutorizado=[]
def validarDatosRegistar():
    usuario = usuarioEntry.get()
    contra1 = contrasennaEntry.get()
    contra2 = contrasennaVerificacionEntry.get()
    validacionUsuario(usuario,contra1,contra2)

def validacionUsuario(usuario, contra1, contra2):
    usuario1=usuario
    if usuario.find("@") != -1:
        dominio = ["gmail.com","hotmail.com","yahoo.com","outlook.com","live.com"]
        usuario = usuario.split('@')
        if usuario[0] == "":
            return messagebox.showwarning("Advertencia","El usuario no puede ser vacío")
        elif usuario[1] not in dominio:
            return messagebox.showwarning("Advertencia","El dominio del usuario está incorrecto")
        else:
            validacionContrasenna(usuario1,contra1,contra2,usuarioAutorizado)
    else:
        return messagebox.showwarning("Advertencia","El correo electrónico no posee '@' ")

def validacionContrasenna(usuario1,contra1,contra2,usuarioAutorizado):
    if 5>len(contra1):
        return messagebox.showwarning("Advertencia","La contraseña debe ser mayor a 4 caracteres.")
    elif len(contra1)>15:
        return messagebox.showwarning("Advertencia","La contraseña debe ser menor a 16 caracteres.")
    else:
        if contra1.isalpha() == True:
            return messagebox.showwarning("Advertencia","La contraseña debe contener al menos un número.")
        elif contra1.isdigit() == True:
            return messagebox.showwarning("Advertencia","La contraseña debe contener al menos una letra.")
        elif contra1.isalnum() == False:
            return messagebox.showwarning("Advertencia","La contraseña no debe contener caracteres especiales.")
        else:
            if str(contra1) != str(contra2):
                return messagebox.showwarning("Advertencia","Las contraseñas no coinciden.")
            else:
                ventanaAceptado = tk.Toplevel()
                ventanaAceptado.resizable(0,0)
                ventanaAceptado.geometry("350x100")
                ventanaAceptado.title("Felicidades")
                Label(ventanaAceptado,text="Usuario y contraseña aceptados. \n Se han guardado los datos en un archivo de texto. \n Cierre y vuelva abrir el programa para ingresar \n a la plataforma del TSE.",fg="black").place(x=40,y=20)
                usuarioAutorizado.append(usuario1)
                usuarioAutorizado.append(contra1)
                file = open("usuarioAutorizado.txt","w")
                file.write(str(usuarioAutorizado))
                file.close
                return

def limpiarEntry1():
    usuarioEntry.delete(0,END)
    contrasennaEntry.delete(0,END)
    contrasennaVerificacionEntry.delete(0,END)

def crearUsuario():
    firstWindow = Tk()
    firstWindow.resizable(0,0)
    firstWindow.title("Registrarse")
    firstWindow.geometry("420x365")

    Label(firstWindow,text="Ingrese un usuario y contraseña para registrarse",fg="black",font="none 12").place(x = 20,y = 25)
    Label(firstWindow,text="Usuario: ",fg="black",font="none 10").place(x=20,y=75)
    Label(firstWindow,text="Contraseña: ",fg="black",font="none 10").place(x=20,y=125)
    Label(firstWindow,text="Verificación contraseña: ",fg="black",font="none 10").place(x=20,y=175)

    valor=""
    global usuarioEntry
    usuarioEntry = Entry(firstWindow, width = 30,textvariable = valor)
    usuarioEntry.place(x=200,y=75)
    usuario = usuarioEntry.get()

    global contrasennaEntry
    contrasennaEntry = Entry(firstWindow, width = 30,textvariable = valor)
    contrasennaEntry.place(x=200,y=125)
    contra1 = contrasennaEntry.get()

    global contrasennaVerificacionEntry
    contrasennaVerificacionEntry = Entry(firstWindow, width = 30,textvariable = valor)
    contrasennaVerificacionEntry.place(x=200,y=175)
    contra2 = contrasennaVerificacionEntry.get()
        
    regist=Button(firstWindow,text="Registrarse",command=validarDatosRegistar,heigh=2,width=40,font="none 12")
    regist.place(x=20,y=225)

    limpiar=Button(firstWindow,text="Limpiar",command=limpiarEntry,heigh=2,width=40,font="none 12")
    limpiar.place(x=20,y=285)
    firstWindow,mainloop()

try:
    file = open("usuarioAutorizado.txt", "r")
    file.close
    ventanaIngresar()

except FileNotFoundError:
    crearUsuario()
