# PRACTICA 5 - PATRONES DE DISEÑO
# Fecha: 29 de septiembre

#- Ejemplo Logger (Singleton) 
class Logger:
    _instancia = None  # Atributo de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        # __new__ controla la creación de instancias antes de __init__
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.archivo = open("app.log", "a")  # archivo de logs
        return cls._instancia  # Devuelve siempre la misma instancia

    def log(self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()  # Guardar en disco


# Uso del Logger
logger1 = Logger()
logger1.log("Inicio de sesión en la aplicación")

logger2 = Logger()
logger2.log("El usuario se autenticó")

# Verificamos si ambos objetos son el mismo
print("Logger Singleton:", logger1 is logger2)  # True



class Presidente:
    _instancia = None  # atributo para la única instancia

    def __new__(cls, nombre):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.nombre = nombre
            cls._instancia.historial = []
        return cls._instancia

    def accion(self, accion):
        evento = f"{self.nombre} ({accion})"
        self.historial.append(evento)
        print(evento)


# Varios presidentes intentan tomar el poder
p1 = Presidente("AMLO")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

p1.accion("abrió una nueva escuela")
p2.accion("descuidó su ciudad")
p3.accion("es buena onda")

print("\nHistorial del presidente:")
print(p1.historial)

print("¿Son la misma instancia?:", p1 is p2 is p3)  # True o False

#1) ¿Qué pasaría si eliminamos la verificación if cls._instancia is None en el método __new__?
#Si se elimina esa verificación, cada vez que creemos un objeto de la clase se generará una nueva instancia, en lugar de reutilizar la misma. En consecuencia,
#  la clase dejaría de comportarse como un Singleton y perderíamos el objetivo de tener un único objeto global.


#2) ¿Qué significa el True en p1 is p2 is p3 en este contexto?
# Significa que todas las variables (p1, p2, p3) apuntan exactamente al mismo objeto en memoria.
# aunque se intentaron crear tres presidentes diferentes, gracias al patrón 
#Singleton solo existe un único presidente compartido por todas las referencias.

#3) ¿Es buena idea usar Singleton para todo lo que sea global? Ejemplo donde no sería recomendable.
#No, no es recomendable usar Singleton para todo lo global, porque puede volver el código rígido y 
# limitar la creación de múltiples objetos necesarios en ciertas situaciones.
