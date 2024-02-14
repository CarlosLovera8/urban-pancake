class Carro:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} ({self.anio})"

class Barco:
    def __init__(self, manufacturer, name, length):
        self.manufacturer = manufacturer
        self.name = name
        self.length = length

    def __str__(self):
        return f"Barco: {self.manufacturer} {self.name} ({self.length} ft)"

class Avion:
    def __init__(self, manufacturer, model, year, capacity):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.capacity = capacity

    def __str__(self):
        return f"Avion: {self.manufacturer} {self.model} ({self.year}), capacidad: {self.capacity}"

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