precio = None
def obtener_precio_usuario(precio):
    precio = int(input("Enter the item's price:\n"))
    return float(precio)
floatprecio= obtener_precio_usuario(precio)
print(floatprecio)