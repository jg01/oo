class Retangulo:
    def __init__(self,base,altura) -> None:
        self.base=base
        self.altura=altura
        
    def mudar_lados(self,nova_base,nova_altura):
        self.base = nova_base
        self.altura = nova_altura
        
    def retornar_lados(self):
        return self.base, self.altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = self.base*2 + self.altura*2
        return perimetro