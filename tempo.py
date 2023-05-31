import time

class Task:
    def __init__(self, description):
        self.description = description

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]

    def execute_task(self):
        if len(self.tasks) == 0:
            print("A lista de tarefas está vazia.")
            return

        task = self.tasks[0]
        print("Executando tarefa:", task.description)

        remaining_time = 15 * 60  # converter para segundos
        start_time = time.time()
        end_time = start_time + remaining_time

        while time.time() < end_time:
            elapsed_time = int(time.time() - start_time)
            remaining_time = max(0, 15 * 60 - elapsed_time)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print("Tempo restante: {:02d}:{:02d}".format(minutes, seconds))

            choice = input("Digite 'C' para marcar como concluída, 'P' para parar a execução: ").lower()
            if choice == "c":
                print("Tarefa marcada como concluída.")
                break
            elif choice == "p":
                print("Execução da tarefa interrompida.")
                return

            time.sleep(1)

        self.tasks.pop(0)
        self.tasks.append(task)

        if len(self.tasks) > 0:
            self.execute_task()
        else:
            print("A lista de tarefas está vazia.")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("A lista de tarefas está vazia.")
            return

        print("Lista de Tarefas:")
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task.description}")

def save_tasks(task_list):
    with open("tarefas.txt", "w") as file:
        for task in task_list.tasks:
            file.write(f"{task.description}\n")

def load_tasks():
    task_list = TaskList()
    try:
        with open("tarefas.txt", "r") as file:
            for line in file:
                description = line.strip()
                task = Task(description)
                task_list.tasks.append(task)
    except FileNotFoundError:
        pass
    return task_list

task_list = load_tasks()

while True:
    print("Menu:")
    print("1. Adicionar tarefa")
    print("2. Executar tarefa")
    print("3. Deletar tarefa")
    print("4. Ver tarefas")
    print("5. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        description = input("Digite a descrição da tarefa: ")
        task_list.add_task(description)
        save_tasks(task_list)
    elif choice == "2":
        task_list.execute_task()
        save_tasks(task_list)
    elif choice == "3":
        index = int(input("Digite o índice da tarefa que deseja deletar: "))
        task_list.delete_task(index)
        save_tasks(task_list)
    elif choice == "4":
        task_list.view_tasks()
    elif choice == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")

