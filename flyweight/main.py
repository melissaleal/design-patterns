from flyweight import createShapesWithFlyweight
from normal import createShapesWithoutFlyweight
from plot import plot_memoryusage

if __name__ == "__main__":
    createShapesWithFlyweight()
    createShapesWithoutFlyweight()
    plot_memoryusage()