import matplotlib.pyplot as plt

def plot_memoryusage():
    types = ['Without flyweight', 'With flyweight']
    memory = [25.8, 25.5]
    
    plt.bar(types, memory, color=['red', 'green'])
    plt.title("Memory usage: Without flyweight vs With flyweight")
    plt.ylabel("Memory (MiB)")
    plt.xlabel("Design Pattern")
    plt.ylim(25.0, 26.0)
    plt.show()