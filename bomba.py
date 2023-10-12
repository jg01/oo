class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel) -> None:
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self, valor):
        c1 = valor/self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - c1)
        return c1
    
    def abastecerPorLitro(self, litro):
        c2 = litro*self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - c2)
        return c2
    
    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo
    
    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade