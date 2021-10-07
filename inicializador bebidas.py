class bebida:
    Agua = True
    Gas = "w"
    Sabor = "x"
    Colorantes = "y"
    Temperatura = "z"
    


    def __init__ (self,a,b,c,d):
        self.Gas = a
        self.Sabor = b
        self.Colorantes = c
        self.Temperatura = d


cocacola = bebida("Con gas", "Sabor cola", "con colorantes", "Fria")
tematcha = bebida("Sin gas", "Sabor matcha", "sin colorantes", "Caliente")
agua = bebida("Sin gas", "Sin sabor", "Sin color", "Fria")


print(cocacola.Gas, cocacola.Sabor, cocacola.Colorantes, cocacola.Temperatura)
print(tematcha.Gas, tematcha.Sabor, tematcha.Colorantes, tematcha.Temperatura)
print(agua.Gas, agua.Sabor, agua.Colorantes, agua.Temperatura)
