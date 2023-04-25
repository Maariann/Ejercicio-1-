class Email:
    __idCuenta = str
    __dominio = str
    __tipoDominio = str
    __contrasena = str
    
    def __init__(self,cuenta=None,dominio=None,tipDominio=None,contra=None):
        self.__idCuenta=cuenta
        self.__dominio=dominio
        self.__tipoDominio=tipDominio
        self.__contrasena=contra
        
    def retornaEmail(self):
        return self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self,correo,cont):
        if (correo.find('@')!= -1):
            auxCorreo= correo.split('@')
            user= auxCorreo[0]
            if (auxCorreo[1].find('.')!= -1):
                domCompleto= auxCorreo[1].split('.')
                auxDominio= domCompleto[0]
                auxTipoDominio= domCompleto[1]
                self.__init__(user,auxDominio,auxTipoDominio,cont)
                print('Correo creado con exito')
            else: print('Error: El dominio no contiene punto')
        else: print ('Error: El correo ingresado no contiene @')
    
    def modificaContra(self):
        actual = input("Ingresa tu contraseña:")
        while self.__contrasena != actual:
            actual = input("Contraseña erronea, intenta nuevamente: ")
        self.__contrasena = input('Ingresa la nueva contraseña:')
        