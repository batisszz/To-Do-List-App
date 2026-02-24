# data/todo_repository.py
class TodoRepository:
    def __init__(self):
        self.__tasks = [] 

    def add(self, task: str):
        self.__tasks.append(task)
        return True

    def get_all(self):
        return self.__tasks