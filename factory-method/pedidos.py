class Pedido:
    def __init__(self, id_pedido, id_cliente, quantidade):
        self.__id_pedido = id_pedido
        self.__id_cliente = id_cliente
        self.__produtos = []
        self.__quantidade = quantidade

    def addProduto(self, produto):
        self.__produtos.append(produto)

    def listProduto(self):
        for produto in self.__produtos:
            produto.exibirInfo()

    @property
    def id_pedido(self):
        return self.__id_pedido
    
    @id_pedido.setter
    def id_pedido(self, value):
        self.__id_pedido = value

    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, value):
        self.__id_cliente = value

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, value):
        self.__quantidade = value

class Produto:
    def exibirInfo():
        pass
    def addPedido(self, pedido):
        pedido.addProduto(self)

class Eletronico(Produto):
    def __init__(self, nome, preco, marca, modelo, sn):
        self.__nome = nome
        self.__preco = preco
        self.__marca = marca
        self.__modelo = modelo
        self.__sn = sn

    def exibirInfo(self):
        print(f"FICHA DE PRODUTO \n Nome: {self.__nome} \n Preço: {self.__preco} \n Marca: {self.__marca} \n Modelo: {self.__modelo} \n Serial Number: {self.__sn} \n")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, value):
        self.__preco = value
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, value):
        self.__marca = value
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, value):
        self.__modelo = value
        
    @property
    def sn(self):
        return self.__sn
    
    @sn.setter
    def sn(self, value):
        self.__sn = value

class Roupa(Produto):
    def __init__(self, categoria, preco, tamanho, cor):
        self.__categoria = categoria
        self.__preco = preco
        self.__tamanho = tamanho
        self.__cor = cor

    def exibirInfo(self):
        print(f"FICHA DE PRODUTO \n Categoria: {self.__categoria} \n Preço: {self.__preco} \n Tamanho: {self.__tamanho} \n Cor: {self.__cor} \n")

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, value):
        self.__categoria = value

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, value):
        self.__preco = value

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, value):
        self.__tamanho = value

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, value):
        self.__cor = value

class Alimento(Produto):
    def __init__(self, categoria, preco, peso, unidade, dtValidade):
        self.__categoria = categoria
        self.__preco = preco
        self.__peso = peso
        self.__unidade = unidade
        self.__dtValidade = dtValidade
    
    def exibirInfo(self):
        print(f"FICHA DE PRODUTO \n Categoria: {self.__categoria} \n Preço: {self.__preco} \n Peso: {self.__peso}{self.__unidade} \n Validade: {self.__dtValidade} \n")

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, value):
        self.__categoria = value
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, value):
        self.__preco = value
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, value):
        self.__peso = value
        
    @property
    def unidade(self):
        return self.__unidade
    
    @unidade.setter
    def unidade(self, value):
        self.__unidade = value
        
    @property
    def dtValidade(self):
        return self.__dtValidade
    
    @dtValidade.setter
    def dtValidade(self, value):
        self.__dtValidade = value

class ProdutoFactory:
    def instanciarProduto(tipo, *args):
        if tipo == 'eletronico':
            return Eletronico(*args)
        elif tipo == 'roupa':
            return Roupa(*args)
        elif tipo == 'alimento':
            return Alimento(*args)
        else:
            raise ValueError("Produto inválido")


factory = ProdutoFactory()

eletronico1 = ['Smartphone', 1500.00, 'Samsung', 'Galaxy S21', '123456789']
eletronico1 = factory.instanciarProduto('eletronico', *eletronico1)
eletronico1.exibirInfo()

eletronico2 = ['Notebook', 4500.00, 'Dell', 'XPS 13', '987654321']
eletronico2 = factory.instanciarProduto('eletronico', *eletronico2)
eletronico2.exibirInfo()

roupa1 = ['Camiseta', 50.00, 'M', 'Azul']
roupa1 = factory.instanciarProduto('roupa', *roupa1)
roupa1.exibirInfo()

roupa2 = ['Calça Jeans', 120.00, 42, 'Preto']
roupa2 = factory.instanciarProduto('roupa', *roupa2)
roupa2.exibirInfo()

alimento1 = ['Arroz', 10.0, 5, 'kg', '2025-12-31']
alimento1 = factory.instanciarProduto('alimento', *alimento1)
alimento1.exibirInfo()

alimento2 = ['Feijão', 8.0, 1, 'kg', '2025-06-30']
alimento2 = factory.instanciarProduto('alimento', *alimento2)
alimento2.exibirInfo()