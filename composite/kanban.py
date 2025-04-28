from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def showDetails(self, lvl = 0):
        pass

class Task(Component):
    def __init__(self, description, priority, duration, assigned):
        self.description = description
        self.priority = priority
        self.duration = duration
        self.assigned = assigned

    def showDetails(self, lvl=0):
        prefix = " " * (lvl * 2)
        print(f"{prefix} Task: {self.description}, {self.priority}, {self.duration}, {self.assigned}")

class Tasklist(Component):
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)
    
    def removeTask(self, task):
        self.tasks.remove(task)

    def showDetails(self, lvl=0):
        prefix = " " * (lvl * 2)
        print(f"{prefix} List: {self.title}")
        for task in self.tasks:
            task.showDetails(lvl+1)

class Project(Component):
    def __init__(self, title):
        self.title = title
        self.lists = []

    def addList(self, list):
        self.lists.append(list)
    
    def removeList(self, list):
        self.lists.remove(list)

    def showDetails(self, lvl=0):
        prefix = " " * (lvl * 2)
        print(f"{prefix} Project: {self.title}")
        for list in self.lists:
            list.showDetails(lvl+1)

if __name__ == "__main__":
    task1 = Task("Login", "Alta", 5, "João")
    task2 = Task("Database", "Média", 8, "Maria")
    task3 = Task("Frontend", "Baixa", 12, "Carlos")

    list1 = Tasklist("Backlog")
    list2 = Tasklist("In progress")
    list3 = Tasklist("Completed")

    list1.addTask(task1)
    list1.addTask(task2)
    list2.addTask(task3)

    project = Project("Project 1")
    project.addList(list1)
    project.addList(list2)
    project.addList(list3)

    project.showDetails()