class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0) -> None:
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
        
    def deposito(self, valor):
        if(valor < 0):
            return 'digite um valor maior que zero'
        else:
            self.saldo+=valor
            return self.saldo
    
    def saque(self, valor):
        if(valor > self.saldo):
            return 'voce nao tem esse valor em conta', self.saldo
        else:
            self.saldo -= valor
            return self.saldo
        
pessoa = ContaCorrente(131-2, 'Rafael', 1000.0)

print(pessoa.nome_correntista)

pessoa.alterarNome('Lulu')

print(pessoa.nome_correntista)

print(pessoa.deposito(500))

print(pessoa.saque(5000))