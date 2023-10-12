class Carro:
    def __init__(self, consumo) -> None:
        self.consumo = consumo
        self.nivelCombustivel = 0
        
    def andar(self, km):
        c1 = km/self.consumo
        self.nivelCombustivel-=c1
        
    def obterGasolina(self):
        return self.nivelCombustivel
    
    def adicionarGasolina(self, litro):
        self.nivelCombustivel+=litro
        

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
