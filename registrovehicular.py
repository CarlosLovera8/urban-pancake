class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} ({self.año})"

class Barco:
    def __init__(self, marca, nombre, longitud):
        self.marca = marca
        self.nombre = nombre
        self.longitud = longitud

    def __str__(self):
        return f"Barco: {self.marca} {self.nombre} ({self.longitud} ft)"

class Avion:
    def __init__(self, marca, modelo, año, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = capacidad

    def __str__(self):
        return f"Avion: {self.marca} {self.modelo} ({self.año}), capacidad: {self.capacity}"

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
