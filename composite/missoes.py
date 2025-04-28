from abc import ABC, abstractmethod

## implementando interface ComponenteMissao 
class ComponenteMissao(ABC):
    @abstractmethod
    def executar():
        pass

class Tarefa(ComponenteMissao):
    def __init__(self, titulo):
        self.titulo = titulo

    def executar(self):
        print(f"Executando tarefa \"{self.titulo}\"")

class Missao(ComponenteMissao):
    def __init__ (self, titulo):
        self.titulo = titulo
        self.children = []

    def addTarefa(self, tarefa):
        self.children.append(tarefa)

    def delTarefa(self, tarefa):
        self.children.remove(tarefa)

    def executar(self):
        print(f"Missão \"{self.titulo}\":")
        for child in self.children:
            child.executar()

if __name__ == "__main__":
    t1 = Tarefa("tarefa 1")
    t2 = Tarefa("tarefa 2")
    t3 = Tarefa("tarefa 3")
    t4 = Tarefa("tarefa 4")
    t5 = Tarefa("tarefa 5")

    mis1 = Missao("missão 1")
    mis2 = Missao("missão 2")

    mis1.addTarefa(t2)
    mis1.addTarefa(t3)
    mis1.addTarefa(t4)
    mis2.addTarefa(t1)
    mis2.addTarefa(t5)

    mis1.executar()
    print()
    mis2.executar()