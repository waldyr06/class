#Waldyr Felype
from datetime import date
import typing
Produto = typing.NewType("Produto", any)
Compra = typing.NewType("Compra", any)

class Pessoa():
    def __init__(self, nome,cpf, telefone,endereco,data_Nascimento):
        self.nome = str(nome) 
        self.cpf = int(cpf) 
        self.telefone = int(telefone) 
        self.endereco = int(endereco) 
        self.data_Nascimento = data_Nascimento

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, data_Nascimento):
        super().__init__(nome, cpf, telefone, endereco, data_Nascimento)
     
        
class Fornecedor(Pessoa):
    def __init__(self,):
        self.catalogo = []
        super().__init__()
        
class Funcionario():
    def __init__(self, nome, salario):
        self.nome = str(nome) 
        self.salario = float(salario)

class Vendedor(Funcionario):
    def __init__(self, estoque):
        self.estoque = {}
        super().__init__()
    
    def ChecarEstoque(self,produto,quantidade)->int:
        if produto in self.estoque and self.estoque[produto] >= quantidade:
            print(f"{self.nome}: {quantidade} unidades de {produto.nome} estão disponíveis no estoque.")
            return True
        else:
            print(f"{self.nome}: Desculpe, não há estoque suficiente de {produto.nome}.")
            return False



class Gerente(Funcionario):
    def __init__(self):
        super().__init__
    def RelatorioProduto(self, produto: Produto) -> int:
        return 0
     
    def FecharCompra(compra: Compra):
        return


class Transacao():
    def __init__(self, transacao_id, cliente):
        self.transacao_id = transacao_id
        self.cliente = str(cliente)
        self.itens = []

class Venda(Transacao):
    def __init__(self, venda_id, cliente, produtos):
        self.venda_id = venda_id
        self.cliente = str(cliente)
        self.produtos = int(produtos)
        self.total = self.calcular_total()

class Compra(Transacao):
    def __init__(self,fornecedor):
        self.fornecedor = Fornecedor

class ItemTransacao():
    def __init__(self,produto, quantidade):
        self.produto = int(Produtos)
        self.quantidade = int(quantidade)

class Produtos():
    def __init__(self, produto_id, nome, preco, custo, imposto):
        self.id = int(produto_id)
        self.nome = str(nome)
        self.preco = int(preco)
        self.custo =int(custo)
        self.imposto = int(imposto)

class RelatorioProduto():
    def __init__(self, produto_id, quantidade, estoque_restante):
        self.produto_id = int(produto_id)
        self.quantidade = int(quantidade)
        self.estoque_restante = int(estoque_restante)
#Fiz o meu melhor na medida do possivel.




