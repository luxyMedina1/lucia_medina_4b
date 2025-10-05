#practica 3. INTRODUCCION AL POLIMORFISMO 
#SIMULAR UN SISTEMA DE COBRO CON MULTIPLES OPCIONES DE PAGO 
#MEDINA LUCIA 
#19 DE SEPTIEMBRE 

class PagoTarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta bancaria"
    
class Transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesando pago con transferencia por la cantidad de ${cantidad}"
    
class Deposito:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por medio de depósito en ventanilla de ${cantidad}"
    
class Paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} por medio de PayPal"
    

# INSTANCIAS
metodos_pago = [PagoTarjeta(), Transferencia(), Deposito(), Paypal()]

for m in metodos_pago:
    print(m.procesar_pago(500))


#ACTIVIDAD; PROCESAR PAGO CON DIFERENTES CANTIDADES EN CADA UNO DE LAS FORMAS  DE PAGO , EJEMPLO ; 
#100
pagos = [
    (PagoTarjeta(), 100),
    (Transferencia(), 500),
    (Paypal(), 2000),
    (Deposito(), 400)
]

#polimofismo (mismo metodo)
print("=== SISTEMA DE COBRO MULTIPLE ===\n")
for metodo, cantidad in pagos:
    print(metodo.procesar_pago(cantidad))


#ACTIVIDAD MOSTRAR NOTIFICACION , POR MENSAJE  QUE DIGA  "" SE MANDO VIA CORREO , EL MENSAJE FUE UN EXITO "" VIA MENSAJE "
