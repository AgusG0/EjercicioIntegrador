class Persona():
    def __init__(self, titular, edad, dni):
        self.titular = titular
        self.edad = edad
        self.dni = dni
       
    def __str__(self) -> str:
         return f'{self.titular} {self.dni}'
   
#getter
    
    def titular(self):
        return self.titular
   
    def edad(self):
        return self.edad
   
    def dni(self):
        return self.dni

#setter

    def titular(self, titular):
        self.titular = titular
   
    def edad(self, edad):
        self.edad = edad

    def dni(self,dni):
        self.dni = dni


class Cuenta(Persona):
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad    
       
    def __str__(self) -> str:
        return f'{self.titular} {self.cantidad}'
   
#getter
    def titular(self):
        return self.titular
   
    def cantidad(self):
        return self.cantidad

#setter

    def titular(self, titular):
        self.titular = titular

    def cantidad(self,cantidad):
        self.cantidad = cantidad

def mostrar(self):
    print("Nombre: ", self.titular)
    print("D.N.I: ", self.dni)
    print("Edad: ", self.edad)
    print("Monto Disponible: ", self.cantidad)

def ingresar(self, cantidad):
    if cantidad <0:
        print("Monto Disponible: ", self.cantidad, "(No tiene saldo negativo)")
    else:
        print("Monto Disponible: ",self.cantidad)

def retirar(self, cantidad):
    print(self.cantidad)


class cuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        self.titular = titular
        self.cantidad = cantidad
        self.bonificacion = bonificacion

    def __str__(self) -> str:
         return f'{self.titular} {self.cantidad}'

#getter
    def bonificacion(self):
        return self.bonificacion

#setter
    def bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        if self.edad >=18 & self.edad <= 25 :
            return True
        else:
            return False 

    def mostrar(self):
        print("Cuenta Joven - Bonificación: ", self.bonificacion)

    def retirar(self, cantidad):
        if self.es_titular_valido():
            return retirar.cantidad
        else:
            print("No puede efectuar un retiro")
    
# Programa Principal

mi_persona = Persona ("Francisca H", "39", "29.477.345")
mi_cuenta = Cuenta("Agustina GO", "370.000")
mi_cuentaJoven = cuentaJoven ("Fernando M", "24", "2.000")
mi_bonificacion = ("2.000")

print("Cuenta: ", mi_cuenta)
print("Cuenta Joven: ", mi_cuentaJoven)
print("Bonificacion: "+ mi_bonificacion + "%")

