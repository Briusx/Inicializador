class barco:
    Transporte = True
    Via = "Agua"
    Tipo = "x"
    Motor = "y"
    Pasajeros = "z"
    


    def __init__ (self,a,b,c):
        self.Tipo = a
        self.Motor = b
        self.Pasajeros = c


barco1 = barco("Ferry", "con motor", "con capacidad para 300 pasajeros")
barco2 = barco("Catamarán", "con motor", "con capacidad para 80 personas")
barco3 = barco("Barco pirata", "sin motor", "con capacidad para 100 personas")


print(barco1.Tipo, barco1.Motor, barco1.Pasajeros)
print(barco2.Tipo, barco2.Motor, barco2.Pasajeros)
print(barco3.Tipo, barco3.Motor, barco3.Pasajeros)
