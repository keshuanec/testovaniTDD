"""
Správa úkolů (OOP)
Vytvořte třídu Task s atributy description (popis úkolu) a completed (boolean určující, zda je úkol dokončen).
Vytvořte třídu TaskManager, která umožňuje přidávat úkoly, označovat úkoly jako dokončené
a vracet seznam dokončených a nedokončených úkolů.

"""

class Task:
    def __init__(self,description,completed = False):
        self.description = description
        self.completed = completed

    def __str__(self):
        state = "nedokoncen"
        if self.completed:
            state = "dokoncen"
        return f"ukol \"{self.description}\" je {state}"

    def __repr__(self):
        state = "nedokoncen"
        if self.completed:
            state = "dokoncen"
        return f"ukol \"{self.description}\" je {state}"

    def __eq__(self, other):
        return self.description == other.description and self.completed == other.completed


class TaskManager:
    def __init__(self):
        self.task_list = []

    def __str__(self):
        result = ""
        for task in self.task_list:
            result += f"{task} \n"
        return result

    def add_task(self,task):
        self.task_list.append(task)

    def completed(self,i: int):
        self.task_list[i-1].completed = True

    def list(self,state):
        """

        :param state: completed, uncompleted, all
        :return:
        """
        result = []
        if state == "completed":
            for task in self.task_list:
                if task.completed:
                    result.append(task)
            return result
        elif state == "uncompleted":
            for task in self.task_list:
                if not task.completed:
                    result.append(task)
            return result
        elif state == "all":
            return self.task_list

        else:
            raise ValueError

if __name__ == "__main__":
    notebook = TaskManager()

    task1 = Task("naucit se python")
    task2 = Task("jit spat")
    task3 = Task("najist se")

    notebook.add_task(task1)
    notebook.add_task(task2)
    notebook.add_task(task3)
    notebook.completed(1)
    print(notebook)
    print("-"*80)
    print(notebook.list("completed"))
    print("-"*80)
    print(notebook.list("uncompleted"))
    print("-"*80)
    print(notebook.list("all"))
    print("-"*80)
    print(notebook.list("hola"))