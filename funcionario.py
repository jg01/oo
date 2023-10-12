class Funcionario():
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario
    
    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    
    def aumentarSalario(self, porcentagemDeAumento=0):
        self.salario += self.salario * (porcentagemDeAumento)/100
    
funcionario = Funcionario('Gil', 10000)
print(f'{funcionario.getNome}, {funcionario.getSalario}')