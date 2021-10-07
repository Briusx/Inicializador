class Auto:
    Nombre = "x"
    Color = "y"
    llantas = 4
    puertas = 4
    Volante = True
    Asientos = 5
    motor = True
    Bolsa_de_aire = True


    def __init__ (self,e,n):
        self.Nombre = e
        self.Color = n

Chevrolet = Auto("camaro","amarillo")
Volkswagen = Auto("beetle", "azul")
Honda = Auto("civic", "gris")

print(Chevrolet.Nombre, Chevrolet.Color)
print(Volkswagen.Nombre, Volkswagen.Color)
print(Honda.Nombre, Honda.Color)

