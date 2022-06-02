#Elaborado por Sebastián Montero Castro & Mariell Sánchez Peraza
#Fecha de creación: 10 de junio de 2018 a las 2:35 P.M.
#Última Edición: 20 de junio a las 12:42 AM
class Persona:
        cita = 0
        tomo = 0
        asient = 0
        nom = ""
        apel = ""
        sexo = ""
        dist = ""
        cant = ""
        prov = ""
        dia = ""
        mes = ""
        anno = ""
        padre = ""
        nacP = ""
        madre = ""
        nacM = ""
        ced = ""

        def __ini__(self,cita,tomo,asient,nombre,apellidos,sexo,distrito,canton,provincia,dia,mes,anno,padre,nacionalidadPadre,madre,nacionalidadMadre,ced):
            self.cita = cita
            self.tomo = tomo
            self.asiento = asient
            self.nombre = nom
            self.apellidos = apel
            self.sexo = sexo
            self.distrito = dist
            self.canton = cant
            self.provincia = prov
            self.dia = dia
            self.mes = mes
            self.anno = anno
            self.padre = padre
            self.nacionalidadPadre = nacP
            self.madre = madre
            self.nacionalidadMadre =nacM
            self.cedula = ced
    #gets
        def getCita(self):
            return self.cita
        def getTomo(self):
            return self.tomo
        def getAsiento(self):
            return self.asiento
        def getNombre(self):
            return self.nombre
        def getApellidos(self):
            return self.apellidos
        def getSexo(self):
            return self.sexo
        def getDistrito(self):
            return self.distrito
        def getCanton(self):
            return self.canton
        def getProvincia(self):
            return self.provincia
        def getDia(self):
            return self.dia
        def getMes(self):
            return self.mes
        def getAnno(self):
            return self.anno
        def getPadre(self):
            return self.padre
        def getNacioPadre(self):
            return self.nacionalidadPadre
        def getMadre(self):
            return self.madre
        def getNacioMadre(self):
            return self.nacionalidadMadre
        def getCedula(self):
            return self.cedula
                      
        #sets
        def setCita(self, pcita):
            self.cita = pcita
        def setTomo(self, ptomo):
            self.tomo = ptomo
        def setAsiento(self, pasiento):
            self.asiento = pasiento
        def setNombre(self, pnom):
            self.nombre = pnom
        def setApellidos(self,pApel):
            self.apellidos = pApel
        def setSexo(self, pSexo):
            self.sexo = pSexo
        def setDistrito(self, pDist):
            self.distrito = pDist
        def setCanton(self, pCant):
            self.canton = pCant
        def setProvincia(self, pProv):
            self.provincia = pProv
        def setDia(self, pDia):
            self.dia = pDia
        def setMes(self, pMes):
            self.mes = pMes
        def setAnno(self, pAnno):
            self.anno = pAnno
        def setPadre(self, pPadre):
            self.padre = pPadre
        def setNacioPadre(self, pNacPadre):
            self.nacionalidadPadre = pNacPadre
        def setMadre(self, pMadre):
            self.madre = pMadre
        def setNacioMadre(self, pNacMadre):
            self.nacionalidadMadre = pNacMadre
        def setCedula(self, pCed):
            self.cedula = pCed

        #mostrar datos

        def mostrarArbol(self):
            return self.nombre + self.apellidos + self.padre + self.madre        
        def indicarDatos(self):
            return [str(self.cita) , str(self.tomo) , str(self.asiento) , self.nombre , self.apellidos , str(self.sexo) , self.distrito , self.canton , self.provincia , str(self.dia) , str(self.mes) , str(self.anno) , self.padre , self.nacionalidadPadre , self.madre , self.nacionalidadMadre]

