
#HOY ES 18 DE SEPTIEMBRE 
#MEDINA LUCIA
#PRACTICA2 ; atributos publicos y privados 

class Persona:  
    def __init__(self, nombre, edad):  # constructor de clases 
        self.nombre = nombre  # atributo publico 
        self.edad = edad  # atributo publico 
        self.__cuenta = None  # atributo privado

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Esta persona cumplió: {self.edad} años")
        
    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene cuenta bancaria.")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es: $ {self.__cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} aún no tiene cuenta bancaria.")
        

class cuenta_bancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo  # atributo privado 

    def mostrar_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositó la cantidad de $ {cantidad}. Nuevo saldo: $ {self.__saldo}")
        else:
            print("Ingresa una cantidad válida.")

    # ACTIVIDAD 1: Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Se retiraron $ {cantidad}. Nuevo saldo: $ {self.__saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("Ingresa una cantidad válida.")



persona1 = Persona("Medina", 20)
cuenta1 = cuenta_bancaria("001", 500)

persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()

cuenta1.depositar(200)
persona1.consultar_saldo()

cuenta1.retirar(100)
persona1.consultar_saldo()

# ACCEDER A LOS ATRIBUTOS PUBLICOS 
print(persona1.nombre)
print(persona1.edad)

