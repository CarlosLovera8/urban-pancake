class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo}: {self.marca} {self.modelo} ({self.anio})"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio, "Carro")

class Barco(Vehiculo):
    def __init__(self, manufacturer, name, length):
        super().__init__(manufacturer, name, length, "Barco")

class Avion(Vehiculo):
    def __init__(self, manufacturer, model, year, capacity):
        super().__init__(manufacturer, model, year, "Avion")

# Crear objetos de diferentes tipos de vehículos
car1 = Carro("Toyota", "Camry", 2020)
car2 = Carro("Honda", "Civic", 2019)
barco1 = Barco("Chris-Craft", "Capri", 25.5)
barco2 = Barco("Boston Whaler", "Montauk", 21.0)
avion1 = Avion("Boeing", "747", 1969, 450)
avion2 = Avion("Airbus", "A320", 1988, 220)

# Imprimir información sobre los vehículos
print(car1)
print(car2)
print(barco1)
print(barco2)
print(avion1)
print(avion2)