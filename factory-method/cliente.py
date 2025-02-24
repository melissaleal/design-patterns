class Cliente:
    def validarDoc():
        pass
    def exibirInfo():
        pass

class PF(Cliente):
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def validarDoc(self):
        return len(self.__cpf) == 14
    
    def exibirInfo(self):
        print(f"Cliente Pessoa Física \n Nome: {self.__nome} \n CPF: {self.__cpf}")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

class PJ(Cliente):
    def __init__(self, nome, cnpj):
        self.__nome = nome
        self.__cnpj = cnpj

    def validarDoc(self):
        return len(self.__cnpj) == 18   
    
    def exibirInfo(self):
        print(f"Cliente Pessoa Jurídica \n Razão Sozial: {self.__nome} \n CNPJ: {self.__cnpj}")
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, value):
        self.__cnpj = value

class PE(Cliente):
    def __init__(self, nome, nif):
        self.__nome = nome
        self.__nif = nif

    def validarDoc(self):
        return len(self.__nif) == 9  
    
    def exibirInfo(self):
        print(f"Cliente Pessoa Jurídica \n Nome: {self.__nome} \n NIF: {self.__nif}")
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def nif(self):
        return self.__nif

    @nif.setter
    def nif(self, value):
        self.__nif = value

class ClienteFactory:
    def instanciarCliente(self, tipo, nome, doc):
        if tipo == 'pf':
            return PF(nome, doc)
        elif tipo == 'pj':
            return PJ(nome, doc)
        elif tipo == 'pe':
            return PE(nome, doc)
        else:
            raise ValueError("Não suportado")
        
factory = ClienteFactory()

melissa = factory.instanciarCliente('pf', 'Melissa Leal', '111.222.333.44')
melissa.exibirInfo()

print(f'\n')

skz = factory.instanciarCliente('pj', 'Stray Kids', '12.345.678/0001-95')
skz.exibirInfo()

print(f'\n')

seungmin = factory.instanciarCliente('pe', 'Kim Seungmin', '123456789')
seungmin.exibirInfo()