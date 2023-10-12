class Tamagushi:
    def __init__(self, nome) -> None:
        self.alegria = 100
        self.nome = nome
        self.idade = 0
        self.fome = 0
        self.saude = 100
        self.Vivo = True
        
    def vivo_morto(self):
        if self.saude > 0:
            self.vivo = True
        else:
            self.Vivo = False
        return self.Vivo
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O novo nome do seu Tamagushi é {self.nome}')
        
    def envelhecer(self):
        if self.idade <= 30:
            self.idade += 1
            print(f'O {self.nome} acabou de fazer mais 1 ano de vida\nidade: {self.idade}')
        else:
            self.saude = 0
            print(f'O {self.nome} passou dessa pra melhor ;-;')
    
    def tempo(self, minutos):
        if self.fome < 100:
            self.fome += minutos*0.1
        else:
            self.saude = 0
            print(f'O {self.nome} passou dessa pra melhor ;-;')
            
    def comer(self, comida):
        if self.fome < 100:
            if comida == 'maca':
                self.fome -= self.fome/5
            elif comida == 'pizza':
                self.fome -= self.fome/2
            elif comida == 'cavalo':
                self.fome = 0
            else:
                print(f'O {self.nome} segue uma dieta restrita, tome cuidado!')
                
    def humor(self):
        self.alegria = (3*self.saude + self.fome + 1*self.idade)/5
        
    def status(self):
        if self.Vivo:
            print(f'nome:{self.nome} saude:{self.saude} fome:{self.fome} idade:{self.idade} humor:{self.humor}')
        else:
            print(f'O {self.nome} ta a 7 palmos da terra')


comidas = ('maca', 'pizza', 'cavalo')

juninho = Tamagushi("Pedrin")
juninho.status()

juninho.alterar_nome("Junin")
juninho.envelhecer()
juninho.tempo(15)
juninho.comer(comidas[0])
juninho.humor()
juninho.status()