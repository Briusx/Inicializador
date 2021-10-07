class celular:
    Pantalla = 1
    Cargador = True
    Camara = True
    Calculadora = True
    Contactos = True
    Marca = "x"
    Tipo = "y"
    Color = "z"
    


    def __init__ (self,a,b,c):
        self.Marca = a
        self.Tipo = b
        self.Color = c
        

celular1 = celular("Apple", "Iphone 13", "rojo")
celular2 = celular("Samsung", "Galaxy s10", "naranja")
celular3 = celular("Huawei", "Mate 20", "azul")


print(celular1.Marca, celular1.Tipo, celular1.Color)
print(celular2.Marca, celular2.Tipo, celular2.Color)
print(celular3.Marca, celular3.Tipo, celular3.Color)
