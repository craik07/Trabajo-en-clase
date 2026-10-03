class Llavero:
    def _init_(self, color, tamaño, material):
        self.color = color
        self.tamaño = tamaño
        self.material = material

    def saludar(self):
        print(f"El color del llavero es {self.color}, "
              f"es hecho de {self.material} "
              f"y tiene un tamaño de {self.tamaño}")