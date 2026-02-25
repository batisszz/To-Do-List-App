class TodoCLI:
    def __init__(self, service):
        self.service = service  # dependency injection

    def run(self):
        print("To-Do List App")

        while True:
            command = input("> ")

            if command == "add":
                task = input("Task: ")
                try:
                    self.service.add_task(task)
                    print(f"Added: {task}")
                except Exception as e:
                    print(f"Error: {e}")

            elif command == "list":
                tasks = self.service.get_all_tasks()
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")

            elif command == "exit":
                break

            else:
                print("Unknown command")