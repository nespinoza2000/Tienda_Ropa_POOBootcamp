# Encapsulamiento, Herencia, Polimorfismo y Abstracción
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio  # Atributo encapsulado
        self._cantidad = cantidad  # Atributo encapsulado

    def obtener_precio(self):
        return self._precio

    def obtener_cantidad(self):
        return self._cantidad

    def reducir_stock(self, cantidad_comprada):
        if cantidad_comprada <= self._cantidad:
            self._cantidad -= cantidad_comprada
        else:
            print(f"Stock insuficiente para {self._nombre}")

    def mostrar_info(self):
        raise NotImplementedError(
            "Este método debe ser sobrescrito por las clases hijas"
        )


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla  # Atributo encapsulado específico para ropa

    def mostrar_info(self):
        # Método sobrescrito (Polimorfismo)
        print(
            f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}, Talla: {self._talla}"
        )


class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


# Clase para manejar la abstracción del carrito y compras
class Carrito:
    def __init__(self):
        self._productos = []  # Lista para almacenar los productos

    def agregar_producto(self, producto, cantidad):
        if producto.obtener_cantidad() >= cantidad:
            self._productos.append((producto, cantidad))
            producto.reducir_stock(cantidad)
            print(f"{cantidad} {producto._nombre}(s) agregados al carrito.")
        else:
            print(f"No hay suficiente stock de {producto._nombre}")

    def mostrar_carrito(self):
        if not self._productos:
            print("El carrito está vacío.")
        else:
            total = 0
            print("Carrito de Compras:")
            for producto, cantidad in self._productos:
                subtotal = producto.obtener_precio() * cantidad
                total += subtotal
                print(f"{producto._nombre} x{cantidad} - ${subtotal:.2f}")
            print(f"Total a pagar: ${total:.2f}")


# Interacción con el Usuario y Carrito de Compras
def main():
    # Crear instancias de Camisa y Pantalón
    camisa = Camisa("Camisa de Hombre", 25.00, 50, "M")
    pantalon = Pantalon("Pantalón de Hombre", 30.00, 30, "L")

    # Crear el carrito de compras
    carrito = Carrito()

    # Simulación de interacción con el usuario
    carrito.agregar_producto(camisa, 2)  # Agrega 2 camisas al carrito
    carrito.agregar_producto(pantalon, 1)  # Agrega 1 pantalón al carrito

    # Mostrar el contenido del carrito y el total a pagar
    carrito.mostrar_carrito()


# Ejecutar el programa
if __name__ == "__main__":
    main()
