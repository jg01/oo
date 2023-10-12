class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, canto1, canto2) -> None:
        self.canto1 = canto1
        self.canto2 = canto2
        
    def encontrarCentro(self):
        x_centro = (self.canto1.x+self.canto2.x)/2
        y_centro = (self.canto1.y+self.canto2.y)/2
        return 'X=' + str(x_centro) + 'Y=' + str(y_centro)
        
def imprimeCentro(self):
    print(f'x: {self.x} y{self.y}')

canto1 = Ponto(0,2)
canto2 = Ponto(5,4)

ret = Retangulo(canto1, canto2)
print('Ponto central: %s' %ret.encontrarCentro())