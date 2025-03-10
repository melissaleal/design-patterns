# Os alunos devem implementar o padrão Abstract Factory para criar veículos de diferentes tipos: Terrestres e Aéreos.

# Cada fábrica deve produzir um veículo e um motor compatíveis com o ambiente:

# Crie interfaces abstratas para veículos e motores.
# Implemente versões concretas para dois tipos de transporte:
# Terrestres (Carro com Motor a Combustão)
# Aéreos (Avião com Motor a Jato)
# Crie uma fábrica abstrata que define a criação de veículos e motores.
# Implemente fábricas concretas que criam os veículos e motores correspondentes ao meio de transporte.
# Crie um cliente que utilize a fábrica correta com base no tipo de transporte escolhido.
# Desafio Extra:
# Adicionar um terceiro tipo de transporte Aquático (Barco com Motor Elétrico).
# Criar um menu interativo para o usuário escolher diferentes modelos de veículos e motores.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def descrever(self):
        pass

    @abstractmethod
    def motorizar(self, motor):
        pass

class Motor(ABC):
    @abstractmethod
    def descrever(self):
        pass

    @abstractmethod
    def montar(self):
        pass

class Carro(Veiculo):
    def descrever(self):
        return "Carro"
    
    def motorizar(self, motor):
        print(f"{self.descrever()} com {motor.descrever()}.")
    
class MotorCombustao(Motor):
    def descrever(self):
        return "Motor a Combustão"
    
    def montar(self):
        return print(f"{self.descrever()} montado com sucesso.")

class Aviao(Veiculo):
    def descrever(self):
        return "Avião"
    
    def motorizar(self, motor):
        return print(f"{self.descrever()} com {motor.descrever()}")
    
class MotorAJato(Motor):
    def descrever(self):
        return "Motor a jato"
    
    def montar(self):
        return print(f"{self.descrever()} montado com sucesso.")

class Barco(Veiculo):
    def descrever(self):
        return "Barco"
    
    def motorizar(self, motor):
        return print(f"{self.descrever()} com {motor.descrever()}")

class MotorEletrico(Motor):
    def descrever(self):
        return "Motor elétrico"
    
    def montar(self):
        return print(f"{self.descrever()} montado com sucesso.")

class TransporteTerrestre(ABC):
    def criar_veiculo(self):
        return Carro()
    
    def criar_motor(self):
        return MotorCombustao()
    
class TransporteAereo(ABC):
    def criar_veiculo(self):
        return Aviao()
    
    def criar_motor(self):
        return MotorAJato()
    
class TransporteAquatico(ABC):
    def criar_veiculo(self):
        return Barco()
    
    def criar_motor(self):
        return MotorEletrico()
    
class FabricaTransporte(ABC):
    @abstractmethod
    def criar_personagem(self):
        pass

    @abstractmethod
    def criar_motor(self):
        pass

def cliente(factory):
    veiculo = factory.criar_veiculo()
    motor = factory.criar_motor()
    veiculo.motorizar(motor)
    motor.montar()

def menu():
    while True:
        print(f"\n MENU DE TRANSPORTES")
        print(f"1 - Criar transporte terrestre")
        print(f"2- Criar transporte aéreo")
        print(f"3 - Criar transporte aquático")
        print(f"4 - Cancelar")
        
        opcao = input("Digite um número: ")
        try:
            opcao = int(opcao)
        except:
            print("Digite um número")
            
        if opcao == 1:
            cliente(TransporteTerrestre())
        elif opcao == 2:
            cliente(TransporteAereo())
        elif opcao == 3:
            cliente(TransporteAquatico())
        elif opcao == 4:
            print(f"Saindo do menu...")
            break
        else:
            print(f"Opção inválida")
            
if __name__ == "__main__":
    menu()