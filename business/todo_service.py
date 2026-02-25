# business/todo_service.py
from data.todo_repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_task(self, task_content: str):
        if not task_content or task_content.strip() == "":
            return False, "Gagal: Isi task tidak boleh kosong!"
        
        self.repository.add(task_content)
        return True, f"Berhasil: Task '{task_content}' ditambahkan."

    def get_all_tasks(self):
        tasks = self.repository.get_all()
        return tasks