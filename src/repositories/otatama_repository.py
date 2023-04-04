#this is where tasks are 
from random import *


class OtatamaRepository:

    def __init__(self) -> None:
        self.tasks = []

    def get_tasks(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def find_tasks_of_user(self, username):
        user_tasks = []
        for task in self.tasks:
            if task["username"] == username:
                user_tasks.append(task)
        return user_tasks

    def create_task(self, title, username):
        task_id = len(self.self.tasks)+1
        task = {"id" : task_id, "title" : title, "username" : username, "done": False}
        self.tasks.append(task)
        return task_id

    def complete_task(self, task_id):
        task = self.get_tasks(task_id)
        if task:
            task["done"] = True

    def abandon_task(self, task_id):
        task = self.get_tasks(task_id)
        if task:
            task["username"] = None
    

    def get_random_tasks(self):
        return choice(self.tasks)

    #def break_for_task(self, task_id):
    #this is for when we later make the break-option possible. rn it is only possible to complete or abandon a task
