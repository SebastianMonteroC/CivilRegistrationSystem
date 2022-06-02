#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM

from tkinter import *
import pickle
from tkinter import messagebox
import TP3_Pag_Princ

def inicializarHTML():
    global listaPersonas
    try:
        archivo = open("RegistroNacimientos.txt","rb")
        listaPersonas = pickle.load(archivo)
        archivo.close()
        print(listaPersonas)
        ventanaCertificado()
    except:
        archivo = open("RegistroNacimientos.txt","wb")
        archivo.close()
        ventanaCertificado()
        
def infoIngresada():
    global personaIng
    personaIng = variablePersona.get()
    buscarIngresado(personaIng,listaPersonas)

def funcionRegresar1():
    TP3_Pag_Princ.paginaPrincipal()
    certificateWindow.destroy()
    
def ventanaCertificado():
    global certificateWindow
    certificateWindow = Tk()
    certificateWindow.title("Certificado de Nacimiento")
    certificateWindow.resizable(0,0)
    certificateWindow.geometry("400x300")
    Label(certificateWindow, text = "- Certificados de Nacimiento -", fg = "black", font = "none 12").place(x = 95, y = 20)
    Label(certificateWindow, text = "Ingrese el número de cédula (con guiones):", fg = "black", font = "none 8").place(x = 90, y = 130)
    BotonCrearCertificado = Button(certificateWindow, text = "Generar Certificado", fg = "black", font = "none 12", command = infoIngresada).place(x = 30, y = 200)
    Button(certificateWindow, text = "Regresar", fg = "black", font = "none 12", command = funcionRegresar1).place(x = 280, y = 200)
    texto1 = ""
    global variablePersona
    variablePersona = Entry(certificateWindow, width = 50, textvariable = texto1)
    variablePersona.place(x = 50, y = 150)
    
def buscarIngresado(personaIng, listaPersonas):
    validacion = 0
    for i in range(0,len(listaPersonas)):
        if personaIng == listaPersonas[i][0] + "-" + listaPersonas[i][1] + "-" + listaPersonas[i][2]:
            tablaHTML(listaPersonas[i])
            break
        else:
            validacion += 1
            continue
    if validacion == len(listaPersonas):
        messagebox.showwarning("Error","Este número no esta registrado.")
        
def tablaHTML(lista):
    Cita = lista[0] + "-" + lista[1] + "-" + lista[2]
    Tomo = lista[1]
    Asiento = lista[2]
    Nombre = lista[3]
    Apellidos = lista[4]
    if lista[5] == "0":
        Sexo = "Masculino"
    elif lista[5] == "1":
        Sexo = "Femenino"
    Distrito = lista[6]
    Canton = lista[7]
    Provincia = lista[8]
    DiaNacimiento = lista[9]
    MesNacimiento = lista[10]
    AnnoNacimiento = lista[11]
    NombrePadre = lista[12]
    NacionalidadPadre = lista[13]
    NombreMadre = lista[14]
    NacionalidadMadre = lista[15]

    f = open('Analisis-' + DiaNacimiento + '-' + MesNacimiento + '-' + AnnoNacimiento + '-' + Cita + '.html','w')
    HTML = """<html>
    <head>
    <style>
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
    }
    </style>
    </head>
    <body>

    <table style="width:70%">
      <tr>
        <th colspan="2">Certificado de Nacimiento</th>
      </tr>
      <tr>
        <td>Al tomo:</td>
        <td> """ + Tomo + """</td>
      </tr>
      <tr>
        <td>Asiento:</td>
        <td>""" + Asiento + """</td>
      </tr>
      <tr>
        <td>Cita:</td>
        <td>""" + Cita + """</td>
      </tr>
      <tr>
        <td>Dice que:</td>
        <td>""" + Nombre + " " + Apellidos + """</td>
      </tr>
      <tr>
        <td>Sexo:</td>
        <td>""" + Sexo + """</td>
      </tr>
      <tr>
        <td>Nacio en:</td>
        <td>""" + Distrito + " " + Canton + " " + Provincia + """ </td>
      </tr>
      <tr>
        <td>El dia:</td>
        <td>""" + DiaNacimiento + "/" + MesNacimiento + "/" + AnnoNacimiento + """</td>
      </tr>
      <tr>
        <td>Padre:</td>
        <td>""" + NombrePadre + """</td>
      </tr>
      <tr>
        <td>Nacionalidad:</td>
        <td>""" + NacionalidadPadre + """</td>
      </tr>
      <tr>
        <td>Madre:</td>
        <td>""" + NombreMadre + """ </td>
      </tr>
      <tr>
        <td>Nacionalidad:</td>
        <td>""" + NacionalidadMadre + """</td>
      </tr>
    </table>

    </body>
    </html>"""

    f.write(HTML)
    f.close()



