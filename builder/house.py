## Implementando a interface Builder, responsável por estabelecer os métodos que todo construtor deve apresentar
from abc import ABC, abstractmethod

class ConstrutorCasa(ABC):
    @abstractmethod
    def construir_fundacao(self):
        pass

    @abstractmethod
    def construir_estrutura(self):
        pass

    @abstractmethod
    def construir_telhado(self):
        pass

    @abstractmethod
    def pintar_casa(self):
        pass

    @abstractmethod
    def mobiliar_casa(self):
        pass
    
    @abstractmethod
    def instalar_piscina(self):
        pass
    
    @abstractmethod
    def planejar_jardim(self):
        pass

    @abstractmethod
    def get_casa(self):
        pass

## Implementando os construtures concretos
class ConstrutorCasaModerna(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação moderna')

    def construir_estrutura(self):
        self.casa.add('Estrutura moderna com janelas amplas')

    def construir_telhado(self):
        self.casa.add('Telhado plano')

    def pintar_casa(self):
        self.casa.add('Pintura branca')

    def mobiliar_casa(self):
        self.casa.add('Móveis minimalistas')

    def instalar_piscina(self):
        self.casa.add('Sem piscina') 
    
    def planejar_jardim(self):
        self.casa.add('Sem jardim') 
    
    def get_casa(self):
        return self.casa

class ConstrutorCasaDeCampo(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação de pedra')

    def construir_estrutura(self):
        self.casa.add('Estrutura de madeira com ambientes aconchegantes')

    def construir_telhado(self):
        self.casa.add('Telhado em duas águas')

    def pintar_casa(self):
        self.casa.add('Cores pastéis')

    def mobiliar_casa(self):
        self.casa.add('Móveis estilo vintage')

    def instalar_piscina(self):
        self.casa.add('Sem piscina') 
    
    def planejar_jardim(self):
        self.casa.add('Sem jardim') 
    

    def get_casa(self):
        return self.casa
    
## Implementando o construtor de casa de luxo

class ConstrutorCasaDeLuxo(ConstrutorCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_fundacao(self):
        self.casa.add('Fundação de mármore')

    def construir_estrutura(self):
        self.casa.add('Estrutura de mármore com janelas amplas')

    def construir_telhado(self):
        self.casa.add('Telhado de luxo')

    def pintar_casa(self):
        self.casa.add('Cores neutras')

    def mobiliar_casa(self):
        self.casa.add('Móveis caríssimos')
        
    def instalar_piscina(self):
        self.casa.add('Piscina com água cristalina')
        
    def planejar_jardim(self):
        self.casa.add('Jardim de rosas')

    def get_casa(self):
        return self.casa
    
## Implementando o produto final: casa
class Casa:
    def __init__(self):
        self.partes = []

    def add(self, parte):
        self.partes.append(parte)

    def descrever(self):
        return ', '.join(self.partes)
    
## Implementando o diretor
class DiretorDeConstrucao:
    def __init__(self, construtor):
        self._construtor = construtor

    def construir_casa(self):
        self._construtor.construir_fundacao()
        self._construtor.construir_estrutura()
        self._construtor.construir_telhado()
        self._construtor.pintar_casa()
        self._construtor.mobiliar_casa()
        self._construtor.instalar_piscina()
        self._construtor.planejar_jardim()
        return self._construtor.get_casa()

## Implementando o código principal
    
def main():
    construtores = {
        '1': ConstrutorCasaModerna(),
        '2': ConstrutorCasaDeCampo(),
        '3': ConstrutorCasaDeLuxo()
    }
    
    while True:
        print("\nOpções de casa")
        print("\n1 - Moderna")
        print("\n2 - De campo")
        print("\n3 - De luxo")
        print("\n4 - Sair")
        
        escolha = input("\nQual casa você deseja construir?")
        
        if escolha == '4':
            print("\nFinalizando...")
            break
        
        if escolha in construtores:
            construtor = construtores[escolha]
            diretor = DiretorDeConstrucao(construtor)
            casa = diretor.construir_casa()
            print(casa.descrever())
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
            
if __name__ == "__main__":
    main()