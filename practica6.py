"""
Ejemplo combinado de los patrones de diseño:
- Factory Method (fábrica) para crear distintos tipos de Productos (bebidas).
- Observer (observador) para notificar a clientes sobre el estado de su pedido.

Caso real simulado: Cafetería con pedidos de bebidas. 
La cafetería crea bebidas con una fábrica (según tipo) y cada pedido es un "Subject" que notifica a los "Observers" (clientes / apps)
cuando el estado del pedido cambia (en preparación, listo, entregado).

Comentarios explicativos (en español) incluidos en el código para exposición en clase.
"""
 
from abc import ABC, abstractmethod
from typing import List, Dict
import time
import threading
import uuid


#  Factory Method (Fábrica)


class Beverage(ABC):
    """Producto abstracto: define la interfaz común para todas las bebidas."""
    def __init__(self, size: str = "M"):
        self.size = size  # S, M, L

    @abstractmethod
    def prepare(self) -> str:
        """Pasos para preparar la bebida (retorna una descripción)."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__} (Tamaño {self.size})"


class Espresso(Beverage):
    def prepare(self) -> str:
        return f"Hacer espresso simple para tamaño {self.size}."


class Latte(Beverage):
    def prepare(self) -> str:
        return f"Vaporizar leche y agregar espresso para un Latte tamaño {self.size}."


class Tea(Beverage):
    def prepare(self) -> str:
        return f"Calentar agua y infusionar té para tamaño {self.size}."


class BeverageFactory:
    """
    Factory: crea instancias de bebidas según un 'tipo' dado.
    Ventaja: centraliza creación y permite añadir nuevas bebidas sin cambiar el código cliente.
    """
    _creators: Dict[str, type] = {
        "espresso": Espresso,
        "latte": Latte,
        "tea": Tea
    }

    @classmethod
    def create_beverage(cls, bev_type: str, size: str = "M") -> Beverage:
        bev_type = bev_type.lower()
        if bev_type not in cls._creators:
            raise ValueError(f"Tipo de bebida desconocido: {bev_type}")
        return cls._creators[bev_type](size=size)


#  Observer (Observador)


class Observer(ABC):
    """Interfaz del observador (ej.: cliente o app que recibe notificaciones)."""
    @abstractmethod
    def update(self, subject: "OrderSubject", message: str):
        pass


class OrderSubject:
    """
    Subject: mantiene la lista de observadores y notifica cuando cambia el estado.
    En este caso, cada pedido es un Subject independiente (tiene su id y estado).
    """
    def __init__(self, order_id: str):
        self.order_id = order_id
        self._observers: List[Observer] = []
        self._state: str = "creado"  # estados: creado -> en_preparacion -> listo -> entregado

    def attach(self, obs: Observer):
        if obs not in self._observers:
            self._observers.append(obs)

    def detach(self, obs: Observer):
        if obs in self._observers:
            self._observers.remove(obs)

    def notify(self, message: str):
        """Notifica a todos los observadores con un mensaje."""
        for obs in list(self._observers):  # lista copia para evitar modificaciones durante iteración
            obs.update(self, message)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: str):
        self._state = value
        # generar mensaje legible y notificar
        msg = f"Pedido {self.order_id}: estado cambiado a '{self._state}'."
        self.notify(msg)


# ---------------------------
# Implementaciones concretas
# ---------------------------

class Customer(Observer):
    """Observador concreto: representa al cliente que debe recibir notificaciones."""
    def __init__(self, name: str):
        self.name = name

    def update(self, subject: OrderSubject, message: str):
        # Aquí podemos simular envío de push, SMS, etc. Para la demo imprimimos en consola.
        print(f"[Notificación a {self.name}] {message}")


class KitchenDisplay(Observer):
    """
    Observador concreto: por ejemplo, una pantalla en cocina que también recibe actualizaciones.
    Puede usarse para mostrar cambios en la cola de preparación.
    """
    def __init__(self):
        self.log: List[str] = []

    def update(self, subject: OrderSubject, message: str):
        # Guardamos un registro y mostramos un mensaje corto
        entry = f"KD recibe -> {message}"
        self.log.append(entry)
        print(f"[KitchenDisplay] {entry}")


# ---------------------------
#  Control de Pedidos (Agregador que usa Factory + Subject)
# ---------------------------

class Order:
    """
    Clase que representa un pedido: combina un Beverage creado por la fábrica
    y un OrderSubject para notificaciones.
    """
    def __init__(self, beverage: Beverage, customer: Customer):
        self.id = str(uuid.uuid4())[:8]  # id corto para la demo
        self.beverage = beverage
        self.subject = OrderSubject(self.id)
        self.customer = customer

        # por defecto, adjuntamos al cliente como observador del pedido
        self.subject.attach(customer)

    def start_preparation(self, kitchen_display: KitchenDisplay = None):
        """
        Simula el flujo de preparación. Cambia estados y notifica observadores.
        Se puede pasar un KitchenDisplay u otros observadores extra.
        """
        if kitchen_display:
            self.subject.attach(kitchen_display)

        # Estado: en preparación
        self.subject.state = "en_preparacion"
        # Simular pasos de preparación (en la vida real aquí iria lógica de cola, tiempo, etc.)
        print(f"[Cocina] Preparando {self.beverage} -> {self.beverage.prepare()}")
        # simulación de tiempo (en demostración usamos sleep corto)
        time.sleep(0.4)  # en una demo real no hay que dormir tanto

        # Estado: listo
        self.subject.state = "listo"
        time.sleep(0.2)

        # Estado: entregado
        self.subject.state = "entregado"
        # una vez entregado, podríamos desuscribir observadores si deseamos
        self.subject.detach(self.customer)
        if kitchen_display:
            self.subject.detach(kitchen_display)


# ---------------------------
#  Simulación / Demo
# ---------------------------

def demo_simulation():
    """
    Simula varios pedidos en paralelo (hilos) para mostrar uso combinado de Factory y Observer.
    Ideal para presentar en clase: explique la responsabilidad de cada clase y muestre la salida.
    """
    # Creamos fábrica y observadores globales
    factory = BeverageFactory()
    kitchen_display = KitchenDisplay()

    # Creamos clientes (observadores)
    alice = Customer("Alicia")
    bob = Customer("Roberto")

    # Creamos bebidas usando la fábrica (Factory)
    bev1 = factory.create_beverage("latte", size="L")
    bev2 = factory.create_beverage("espresso", size="S")
    bev3 = factory.create_beverage("tea", size="M")

    # Creamos pedidos (cada pedido es un Subject con sus observadores)
    order1 = Order(bev1, alice)
    order2 = Order(bev2, bob)
    order3 = Order(bev3, alice)

    # Adjuntamos la KitchenDisplay para monitorizar todos los pedidos
    order1.subject.attach(kitchen_display)
    order2.subject.attach(kitchen_display)
    order3.subject.attach(kitchen_display)

    # Simulamos preparación concurrente con hilos (para efecto didáctico)
    threads = [
        threading.Thread(target=order1.start_preparation, args=(kitchen_display,)),
        threading.Thread(target=order2.start_preparation, args=(kitchen_display,)),
        threading.Thread(target=order3.start_preparation, args=(kitchen_display,))
    ]

    for t in threads:
        t.start()
        time.sleep(0.1)  # ligeras desincronizaciones para que la salida sea clara

    for t in threads:
        t.join()

    # Mostrar log de la KitchenDisplay al final
    print("\n--- Log de KitchenDisplay ---")
    for entry in kitchen_display.log:
        print(entry)


if __name__ == "__main__":
    demo_simulation()
