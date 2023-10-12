class Quadrado:
    def __init__(self, lado) -> None:
        if(lado > 0):
            self.lado = lado
        else:
            print('Insira um valor maior que zero para o lado.')
        
    def mudar_lado(self, novo_lado):
        if(novo_lado > 0):
            self.lado = novo_lado
        else:
            print('Insira um novo lado maior que zero.')
            
    def retorna_lado(self):
        return self.lado
    
    def calcula_area(self):
        area = self.lado**2
        return area
    
quadrado = Quadrado(5)

print(quadrado.retorna_lado())
print(quadrado.calcula_area())

quadrado.mudar_lado(10)

print(quadrado.retorna_lado())
print(quadrado.calcula_area())