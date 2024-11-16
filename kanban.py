class KanbanBoard:
    def __init__(self):
        self.columns = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }

    def add_task(self, task):
        """Agrega una tarea a la columna 'To Do'."""
        self.columns["To Do"].append(task)
        print(f"Tarea '{task}' agregada a 'To Do'.")

    def move_task(self, task, from_column, to_column):
        """Mueve una tarea de una columna a otra."""
        if task in self.columns[from_column]:
            self.columns[from_column].remove(task)
            self.columns[to_column].append(task)
            print(f"Tarea '{task}' movida de '{from_column}' a '{to_column}'.")
        else:
            print(f"La tarea '{task}' no se encuentra en '{from_column}'.")

    def show_board(self):
        """Muestra el tablero Kanban."""
        print("\nTablero Kanban:")
        for column, tasks in self.columns.items():
            print(f"{column}: {', '.join(tasks) if tasks else 'Sin tareas'}")
        print()


# Uso del sistema Kanban
kanban = KanbanBoard()

# Agregar tareas
kanban.add_task("Escribir informe")
kanban.add_task("Revisar código")
kanban.add_task("Preparar presentación")

# Mostrar el tablero
kanban.show_board()

# Mover tareas
kanban.move_task("Escribir informe", "To Do", "In Progress")
kanban.move_task("Revisar código", "To Do", "In Progress")
kanban.move_task("Escribir informe", "In Progress", "Done")

# Mostrar el tablero actualizado
kanban.show_board()
