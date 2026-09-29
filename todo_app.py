class TodoApp:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed!")
        else:
            print("Task not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        else:
            print("\n--- Your To-Do List ---")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

# Example Usage
todo = TodoApp()
todo.add_task("Learn Python OOP")
todo.add_task("Complete Chili Research Task Manager")
todo.view_tasks()
todo.remove_task("Learn Python OOP")
todo.view_tasks()
