# diagosticao_Lucia.py
# Simulación de pedidos
# Conceptos básicos: variables, inputs, condicionales, funciones y bucles

# Elegir una temática de tienda y escribir 3 productos
productos = ["Coca Cola", "Agua", "Peñafiel Aguas Naturales"]
precios = [50, 70, 40]

# Función para calcular total
def calcular_total(cantidad, precios):
    total = 0
    for i in range(len(cantidad)):
        total += cantidad[i] * precios[i]
    return total

# Menú
print("Menú de bebidas refrescantes")
nombre = input("Ingresa tu nombre: ")

cantidades = []

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} deseas? "))
    cantidades.append(cantidad)

total = calcular_total(cantidades, precios)

print(f"\n{nombre}, el total de tu compra es: ${total}")
print(f"\n{nombre}, el total de  tu compra es  : ${total}")