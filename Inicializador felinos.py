class felino:
    Reino = "animalia"
    Filo = "Chordata"
    Clase = "Mamífero"
    Orden = "Carnívoro"
    Bigotes = True
    Depredador = True
    Especie = "x"


    def __init__ (self,y):
        self.Especie = y
        

felino1 = felino("gato")
felino2 = felino("leon")
felino3 = felino("pantera")

print(felino1.Especie)
print(felino2.Especie)
print(felino3.Especie)

