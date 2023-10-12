class Macaco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.bucho = []
        
    def comer(self, comida):
        self.bucho.append(comida)
        print(f'{self.nome} comeu {comida}')
    
    def verBucho(self):
        print('Bucho: ', self.bucho)
    
    def digerir(self):
        if len(self.bucho) > 0:
            comida_digerida = self.bucho.pop(0)
            print(f'{self.nome} digeriu a {comida_digerida}')
        else:
            print('N tem nada pra digerir')
            
macaco1 = Macaco('Cesar')
macaco2 = Macaco('Koba')

macaco1.comer(macaco2)

macaco1.verBucho()