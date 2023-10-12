class Tv:
    def __init__(self) -> None:
        self.ligada = False
        self.canal = 1
        self.volume = 10
    
    def ligar(self):
        self.ligada = not self.ligada
        
        if self.ligada:
            print('A tv esta ligada')
        else:
            print('A tv esta desligada')
            
    def trocar_canal(self, canal):
        if self.ligada:
            if 1<=canal<=300:
                self.canal = canal
                print(f'Vc esta no canal {self.canal}')
            else:
                print('Canal fora da faixa (1 a 300)')
        else:
            print('Ligue a TV')
    
    def aumentar_volume(self):
        if self.ligada:
            if self.volume <= 100:
                self.volume += 1
                print(f'O volume esta em {self.volume}')
            else:
                print('Volume maximo')
        else:
            print('Ligue a TV')
        
    def diminuir_volume(self):
        if self.ligada:
            if 0 <= self.volume :
                self.volume += 1
                print(f'O volume esta em {self.volume}')
            else:
                print('Volume minimo')
        else:
            print('Ligue a TV')
            