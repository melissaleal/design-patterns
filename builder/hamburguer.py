## Passo 1: implementar a interface
from abc import ABC, abstractmethod

class HamburguerBuilder(ABC):
    @abstractmethod
    def addBread(self):
        pass
    
    @abstractmethod
    def addMeat(self):
        pass
    
    def addChicken(self):
        pass
    
    def addFish(self):
        pass
    
    @abstractmethod
    def addCheese(self):
        pass
    
    @abstractmethod
    def addVeggies(self):
        pass
    
    @abstractmethod
    def addSpices(self):
        pass
    
    @abstractmethod
    def getResult(self):
        pass
    
## Passo 2: implementar classes concretas para cada tipo de hamburguer

class ClassicburguerBuilder(HamburguerBuilder):
    def __init__(self):
        self.hamburguer = Hamburguer()
        
    def addBread(self):
        self.hamburguer.ingredients.append("Classic Bread")
        return self
    
    def addMeat(self):
        self.hamburguer.ingredients.append("Meat")
        return self
    
    def addCheese(self):
        self.hamburguer.ingredients.append("Cheese")
        return self
    
    def addVeggies(self):
        self.hamburguer.ingredients.append("Veggies")
        return self
    
    def addSpices(self):
        self.hamburguer.ingredients.append("Spices")
        return self
    
    def getResult(self):
        return self.hamburguer

class CheeseburguerBuilder(HamburguerBuilder):
    def __init__(self):
        self.hamburguer = Hamburguer()
        
    def addBread(self):
        self.hamburguer.ingredients.append("Bread")
        return self
    
    def addMeat(self):
        self.hamburguer.ingredients.append("Meat")
        return self
    
    def addCheese(self):
        self.hamburguer.ingredients.append("Cheese")
        return self
    
    def addVeggies(self):
        self.hamburguer.ingredients.append("Veggies")
        return self
    
    def addSpices(self):
        self.hamburguer.ingredients.append("Spices")
        return self
    
    def getResult(self):
        return self.hamburguer

class VeggieburguerBuilder(HamburguerBuilder):
    def __init__(self):
        self.hamburguer = Hamburguer()
        
    def addBread(self):
        self.hamburguer.ingredients.append("Bread")
        return self
    
    def addMeat(self):
        self.hamburguer.ingredients.append("Meat")
        return self
    
    def addCheese(self):
        self.hamburguer.ingredients.append("Cheese")
        return self
    
    def addVeggies(self):
        self.hamburguer.ingredients.append("Veggies")
        return self
    
    def addSpices(self):
        self.hamburguer.ingredients.append("Spices")
        return self
    
    def getResult(self):
        return self.hamburguer

class ChickenburguerBuilder(HamburguerBuilder):
    def __init__(self):
        self.hamburguer = Hamburguer()
        
    def addBread(self):
        self.hamburguer.ingredients.append("Bread")
        return self
    
    def addChicken(self):
        self.hamburguer.ingredients.append("Chicken")
        return self
    
    def addMeat(self):
        self.hamburguer.ingredients.append("Meat")
        return self
    
    def addCheese(self):
        self.hamburguer.ingredients.append("Cheese")
        return self
    
    def addVeggies(self):
        self.hamburguer.ingredients.append("Veggies")
        return self
    
    def addSpices(self):
        self.hamburguer.ingredients.append("Spices")
        return self
    
    def getResult(self):
        return self.hamburguer

class FishburguerBuilder(HamburguerBuilder):
    def __init__(self):
        self.hamburguer = Hamburguer()
        
    def addBread(self):
        self.hamburguer.ingredients.append("Bread")
        return self
    
    def addFish(self):
        self.hamburguer.ingredients.append("Fish")
        return self
    
    def addMeat(self):
        self.hamburguer.ingredients.append("Meat")
        return self
    
    def addCheese(self):
        self.hamburguer.ingredients.append("Cheese")
        return self
    
    def addVeggies(self):
        self.hamburguer.ingredients.append("Veggies")
        return self
    
    def addSpices(self):
        self.hamburguer.ingredients.append("Spices")
        return self
    
    def getResult(self):
        return self.hamburguer
            
## Passo 3: definir produto
    
class Hamburguer:
    def __init__(self):
        self.ingredients = []
        
    def __str__(self):
        return f"Hamburguer com {', '.join(self.ingredients)}"
        
## Passo 4: implementar o diretor

class Chef:
    def __init__(self, builder):
        self.builder = builder
        
    def constructClassicburguer(self):
        return (self.builder.addBread().addMeat().addCheese().addVeggies().addSpices().getResult())
    
    def constructCheeseburguer(self):
        return (self.builder.addBread().addMeat().addCheese().addSpices().getResult())
    
    def constructVeggieburguer(self):
        return (self.builder.addBread().addVeggies().addSpices().getResult())
    
    def constructChickenburguer(self):
        return (self.builder.addBread().addChicken().addVeggies().addSpices().getResult())
    
    def constructFishburguer(self):
        return (self.builder.addBread().addFish().addVeggies().addSpices().getResult())
        
if __name__ == "__main__":
    classicbuilder = ClassicburguerBuilder()
    cheeseburguerbuilder = CheeseburguerBuilder()
    veggieburguerbuilder = VeggieburguerBuilder()
    chickenburguerbuilder = ChickenburguerBuilder()
    fishburguerbuilder = FishburguerBuilder()
    
    chef = Chef(classicbuilder)
    classicburguer = chef.constructClassicburguer()
    print(classicburguer)
    
    chef = Chef(cheeseburguerbuilder)
    cheeseburguer = chef.constructCheeseburguer()
    print(cheeseburguer)
    
    chef = Chef(veggieburguerbuilder)
    veggieburguer = chef.constructVeggieburguer()
    print(veggieburguer)
    
    chef = Chef(chickenburguerbuilder)
    chickenburguer = chef.constructChickenburguer()
    print(chickenburguer)
    
    chef = Chef(fishburguerbuilder)
    fishburguer = chef.constructFishburguer()
    print(fishburguer)