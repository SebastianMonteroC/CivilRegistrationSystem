#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pickle
from TP3_clases import *
import TP3_Pag_Princ

try:
    archivo = open("RegistroNacimientos.txt","rb")
    info = pickle.load(archivo)
    registro1.append(info)
    archivo.close()
except:
    registro1 = []

def informacionIngresada():
    global citaIng,tomoIng,asiIng,nomIng,apeIng,disIng,cantIng,provIng,padreIng,nacioPadreIng,madreIng,nacioMadreIng,sexoIng,diaIng,mesIng,annoIng,cedulaIng, nuevaPersona
    citaIng = cita.get()
    tomoIng = tomo.get()
    asiIng = asiento.get()
    nomIng = nombre.get()
    apeIng = apellido.get()
    disIng = distrito.get()
    cantIng = canton.get()
    provIng = provincia.get()
    padreIng = padre.get()
    nacioPadreIng = variableNacionalidadPapa.get()
    madreIng = madre.get()
    nacioMadreIng = variableNacionalidadMama.get()
    sexoIng = sexo.get()
    diaIng = variableDia.get()
    mesIng = variableMes.get()
    annoIng = variableAnno.get()
    cedulaIng = cita.get() + tomo.get() + asiento.get()
    nuevaPersona = Persona()
    validarInformacion()

def validarInformacion():
    if len(citaIng) != 1:
        messagebox.showwarning("Error","El largo de la cita debe ser uno.")
    elif len(tomoIng) != 4:
        messagebox.showwarning("Error","El largo del tomo debe ser de 4.")
    elif len (asiIng) != 4:
        messagebox.showwarning("Error","El largo del  asiento debe ser de 4.")
    elif tomoIng.isdigit() == False or citaIng.isdigit() == False or asiIng.isdigit() == False:
        messagebox.showwarning("Error","La cita solo puede contener valores numéricos.")
    elif nomIng == "" or apeIng == "" or disIng == "" or cantIng == "" or provIng == "" or padreIng == "" or madreIng == "" or diaIng == "" or mesIng == "" or annoIng == "" or nacioMadreIng == "" or nacioPadreIng == "":
        messagebox.showwarning("Error","Se deben rellenar todos los espacios.")
    elif apeIng.find(" ") == -1:
        messagebox.showwarning("Error","La persona ingresada debe contener dos apellidos.")
    elif padreIng.find(" ") == -1:
        messagebox.showwarning("Error","El padre ingresado debe contener dos apellidos.")
    elif madreIng.find(" ") == -1:
        messagebox.showwarning("Error","La madre ingresada debe contener dos apellidos.")
    elif disIng.isalpha() == False or cantIng.isalpha() == False:
        messagebox.showwarning("Error","El distrito y cantón no pueden contener valores numéricos ni caracteres especiales.")
    elif provIng.lower() not in ["cartago","limón","limon","san jose","san josé","puntarenas","heredia","alajuela","guanacaste"]:
        messagebox.showwarning("Error","Provincia inválida.")
    else:
        nombreValidacion = nomIng
        apellidoValidacion = apeIng
        padreValidacion = padreIng 
        madreValidacion = madreIng
        padres = padreValidacion + madreValidacion
        apellidoValidacion = apellidoValidacion.replace(" ","")
        nombreValidacion = nombreValidacion.replace(" ","")
        padres = padres.replace(" ","")
        if nombreValidacion.isalpha() == False:
            messagebox.showwarning("Error","El nombre de la persona ingresada no pueden contener caracteres especiales o números.")
        elif apellidoValidacion.isalpha() == False:
            messagebox.showwarning("Error","Los apellidos de la persona ingresada no pueden contener caracteres especiales o números.")
        elif padres.isalpha() == False:
            messagebox.showwarning("Error","Los apellidos de los padres no pueden contener caracteres especiales o números.")
        else:
            nuevaPersona = Persona()
            nuevaPersona.setCita(citaIng)
            nuevaPersona.setTomo(tomoIng)
            nuevaPersona.setAsiento(asiIng)
            nuevaPersona.setNombre(nomIng)
            nuevaPersona.setApellidos(apeIng)
            nuevaPersona.setSexo(sexoIng)
            nuevaPersona.setDistrito(disIng)
            nuevaPersona.setCanton(cantIng)
            nuevaPersona.setProvincia(provIng)
            nuevaPersona.setDia(diaIng)
            nuevaPersona.setMes(mesIng)
            nuevaPersona.setAnno(annoIng)
            nuevaPersona.setPadre(padreIng)
            nuevaPersona.setNacioPadre(nacioPadreIng)
            nuevaPersona.setMadre(madreIng)
            nuevaPersona.setNacioMadre(nacioMadreIng)
            nuevaPersona.setCedula(cedulaIng)
            registro1.append(nuevaPersona.indicarDatos())
            guardarBinario(registro1)
            
def guardarBinario(registro1):
    file = open("RegistroNacimientos.txt","wb")
    pickle.dump(registro1, file)
    file.close()
    messagebox.showwarning("Advertencia","Ha agregado una persona al registro. Se han guardado los datos exitosamente.")

def limpiarEntryRegistrar():
    cita.delete(0,END)
    tomo.delete(0,END)
    asiento.delete(0,END)
    nombre.delete(0,END)
    apellido.delete(0,END)
    distrito.delete(0,END)
    canton.delete(0,END)
    provincia.delete(0,END)
    padre.delete(0,END)
    madre.delete(0,END)
    variableDia.set("")
    variableMes.set("")
    variableAnno.set("")
    variableNacionalidadPapa.set("")
    variableNacionalidadMama.set("")

def funcionRegresar():
    TP3_Pag_Princ.paginaPrincipal()
    SignupWindow.destroy()
    
def ventanaRegistrar():
    global SignupWindow
    SignupWindow = Tk()
    SignupWindow.title("Tribunal Supremo de Elecciones")
    SignupWindow.resizable(0,0)
    SignupWindow.geometry("500x600")

    Label(SignupWindow, text = "Datos de la nueva persona", fg = "black", font = "none 18").place(x =  110,y = 15)
    Label(SignupWindow, text = "Cita:", fg = "black", font = "none 12").place(x = 30, y = 60)
    Label(SignupWindow, text = "-", fg = "black", font = "none 12").place(x = 165, y = 57)
    Label(SignupWindow, text = "-", fg = "black", font = "none 12").place(x = 244, y = 57)
    Label(SignupWindow, text = "Nombre:", fg = "black", font = "none 12").place(x =  30, y = 90)
    Label(SignupWindow, text = "Apellidos:", fg = "black", font = "none 12").place(x =  30, y = 125)
    Label(SignupWindow, text = "Sexo:", fg = "black", font = "none 12").place(x =  30, y = 160)
    Label(SignupWindow, text = "Distrito:", fg = "black", font = "none 12").place(x =  30, y = 190)
    Label(SignupWindow, text = "Cantón:", fg = "black", font = "none 12").place(x =  30, y = 220)
    Label(SignupWindow, text = "Provincia:", fg = "black", font = "none 12").place(x =  30, y = 250)
    Label(SignupWindow, text = "Día:", fg = "black", font = "none 12").place(x =  30, y = 280)
    Label(SignupWindow, text = "Mes:", fg = "black", font = "none 12").place(x =  30, y = 320)
    Label(SignupWindow, text = "Año:", fg = "black", font = "none 12").place(x =  30, y = 360)
    Label(SignupWindow, text = "Padre:", fg = "black", font = "none 12").place(x =  30, y = 400)
    Label(SignupWindow, text = "Nacionalidad:", fg = "black", font = "none 12").place(x =  30, y = 430)
    Label(SignupWindow, text = "Madre:", fg = "black", font = "none 12").place(x =  30, y = 470)
    Label(SignupWindow, text = "Nacionalidad:", fg = "black", font = "none 12").place(x =  30, y = 500)

    texto = ""
    global cita, tomo, asiento, nombre, apellido, distrito, canton, provincia, padre, madre, sexo
    cita = Entry(SignupWindow, width = 5, textvariable = texto)
    cita.place(x = 130, y = 60)
    tomo = Entry(SignupWindow, width = 10, textvariable = texto)
    tomo.place(x = 178, y = 60)
    asiento = Entry(SignupWindow, width = 10, textvariable = texto)
    asiento.place(x = 255, y = 60)
    nombre = Entry(SignupWindow, width = 50, textvariable = texto)
    nombre.place(x =  130, y = 90)
    apellido = Entry(SignupWindow, width = 50, textvariable = texto)
    apellido.place(x =  130, y = 125)
    distrito = Entry(SignupWindow, width = 50, textvariable = texto)
    distrito.place(x =  130, y = 190)
    canton = Entry(SignupWindow, width = 50, textvariable = texto)
    canton.place(x =  130, y = 220)
    provincia = Entry(SignupWindow, width = 50, textvariable = texto)
    provincia.place(x =  130, y = 250)
    padre = Entry(SignupWindow, width = 50, textvariable = texto)
    padre.place(x = 130, y = 400)
    madre = Entry(SignupWindow, width = 50, textvariable = texto)
    madre.place(x = 130, y = 470)

    sexo = IntVar()
    Radiobutton(SignupWindow, text = "Masculino", variable = sexo, value = 0).place(x = 123, y = 160)
    Radiobutton(SignupWindow, text = "Femenino", variable = sexo, value = 1).place(x = 220, y = 160)

    global variableDia, variableMes, variableAnno, variableNacionalidadPapa, variableNacionalidadMama
    variableDia = StringVar(SignupWindow)
    OptionMenu(SignupWindow, variableDia, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31).place(x = 134, y = 280)
    variableMes = StringVar(SignupWindow)
    OptionMenu(SignupWindow, variableMes, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).place(x = 134, y = 320)
    variableAnno = StringVar(SignupWindow)
    OptionMenu(SignupWindow, variableAnno, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943, 1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924, 1923, 1922, 1921, 1920, 1919, 1918, 1917, 1916, 1915, 1914, 1913, 1912, 1911, 1910, 1909, 1908, 1907, 1906, 1905, 1904, 1903, 1902, 1901, 1900).place(x = 134, y = 360)

    variableNacionalidadPapa = StringVar(SignupWindow)
    variableNacionalidadPapa.set("Costarricense")
    OptionMenu(SignupWindow, variableNacionalidadPapa, "Costarricense", "Nicaraguense", "Panameño", "Estadounidense","Colombiano","Chino","Venezolano","Otra").place(x = 135, y = 427)
    variableNacionalidadMama = StringVar(SignupWindow)
    variableNacionalidadMama.set("Costarricense")
    OptionMenu(SignupWindow, variableNacionalidadMama, "Costarricense", "Nicaraguense", "Panameña", "Estadounidense","Colombiana","China","Venezolana","Otra").place(x = 135, y = 497)

    Button(SignupWindow, text = "Registrar", fg = "black", font = "none 10", height = 2, width = 15,command = informacionIngresada).place(x = 30, y = 540)
    Button(SignupWindow, text  = "Limpiar", fg = "black", font = "none 10", height = 2, width = 15, command = limpiarEntryRegistrar).place(x = 190, y = 540)
    Button(SignupWindow, text  = "Regresar", fg = "black", font = "none 10", height = 2, width = 15, command = funcionRegresar).place(x = 350, y = 540)



