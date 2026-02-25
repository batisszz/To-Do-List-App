# presentation/cli_controller.py
from business.todo_service import TodoService

class TodoCLI:
    def __init__(self, service: TodoService):
        self.service = service

    def run(self):
        print("=== APLIKASI TODO ===")
        while True:
            print("\nMenu: add | list | exit")
            command = input("> ").lower().strip()

            if command == "add":
                content = input("Isi Task: ")
                success, message = self.service.add_task(content)
                print(message)

            elif command == "list":
                tasks = self.service.get_all_tasks()
                if not tasks:
                    print("Belum ada task.")
                else:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")

            elif command == "exit":
                print("Keluar dari program...")
                break
            else:
                print("Perintah tidak dikenal.")