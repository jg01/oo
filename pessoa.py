class Pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos = 1):
        self.idade += anos
        if self.idade < 21:
            self.crescer = (0.5*anos)
        
    def engordar(self, gordura):
        self.peso += gordura
        
    def emagrecer(self, perda_gordura):
        self.peso -= perda_gordura
        
    def crescer(self, altura_ganha):
        self.altura += altura_ganha