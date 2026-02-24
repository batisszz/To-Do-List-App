    # main.py
from data.todo_repository import TodoRepository
from business.todo_service import TodoService
from presentation.cli_controller import TodoCLI

def main():
    repo = TodoRepository()
    service = TodoService(repo)
    app = TodoCLI(service)
    app.run()

if __name__ == "__main__":
    main()