class cuentaCorriente:

    def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.nif = nif
        self.saldo = saldo

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        self.nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getApellidos(self):
        self.apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        self.telefono

    def setNif(self, nif):
        self.nif = nif

    def getNif(self):
        self.nif

    def setSaldo(self, saldo):
        self.saldo = int(saldo)

    def getSaldo(self):
        return self.saldo

    def retirarDinero(self, cantidad):
        self.setSaldo(self.getSaldo() - int(cantidad))

    def ingresarDinero(self, cantidad):
        self.setSaldo(self.getSaldo() + int(cantidad))

    def consultarCuenta(self):
        usuario = "Usuario: " + str(self.nombre) + " " + str(self.apellidos)
        identificacion = "Con DNI: " + str(self.nif)
        numeroDeTelefono = "Numero de telefono: " + str(self.telefono)
        domicilio = "Domicilio: " + str(self.direccion)

        print (usuario, " identificacion" + "\n",
               numeroDeTelefono + "\n", domicilio)

    def saldoNegativo(self, saldo):
        if get.saldo() < 0:
            return True
        else:
            return False
