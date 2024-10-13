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
        # Método Polimorfismo
        print(
            f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}, Talla: {self._talla}"
        )


# Ropa de Hombre
class Chaqueta(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


# Ropa de Mujer
class Falda(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Blusa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Vestido(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


# Zapatos
class Zapatos(Producto):
    def __init__(self, nombre, precio, cantidad, talla_calzado):
        super().__init__(nombre, precio, cantidad)
        self._talla_calzado = (
            talla_calzado  # Atributo encapsulado específico para zapatos
        )

    def mostrar_info(self):
        # Método Polimorfismo
        print(
            f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}, Talla de Calzado: {self._talla_calzado}"
        )


class ZapatosHombre(Zapatos):
    def __init__(self, nombre, precio, cantidad, talla_calzado):
        super().__init__(nombre, precio, cantidad, talla_calzado)


class ZapatosMujer(Zapatos):
    def __init__(self, nombre, precio, cantidad, talla_calzado):
        super().__init__(nombre, precio, cantidad, talla_calzado)


# Clase para manejar la abstracción del carrito y compras
class Carrito:
    def __init__(self):
        self._productos = []

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
    # Crear instancias de Ropa de Hombre
    camisa = Camisa("Camisa de Hombre", 25.00, 50, "M")
    pantalon = Pantalon("Pantalón de Hombre", 30.00, 30, "L")
    chaqueta = Chaqueta("Chaqueta de Hombre", 55.00, 20, "G")

    # Crear instancias de Ropa de Mujer
    falda = Falda("Falda de Mujer", 28.00, 15, "S")
    blusa = Blusa("Blusa de Mujer", 22.00, 40, "M")
    vestido = Vestido("Vestido de Mujer", 45.00, 10, "L")

    # Crear instancias de Zapatos
    zapatos_hombre = ZapatosHombre("Zapatos de Hombre", 60.00, 25, 42)
    zapatos_mujer = ZapatosMujer("Zapatos de Mujer", 50.00, 20, 38)

    # Crear el carrito de compras
    carrito = Carrito()

    # Simulación de interacción con el usuario
    carrito.agregar_producto(camisa, 2)
    carrito.agregar_producto(pantalon, 1)
    carrito.agregar_producto(chaqueta, 5)
    carrito.agregar_producto(falda, 1)
    carrito.agregar_producto(zapatos_hombre, 1)
    carrito.agregar_producto(zapatos_mujer, 2)
    carrito.agregar_producto(blusa, 2)
    carrito.agregar_producto(vestido, 2)

    # Mostrar el contenido del carrito y el total a pagar
    carrito.mostrar_carrito()


# Ejecutar el programa
if __name__ == "__main__":
    main()
