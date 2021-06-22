from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


TODOS = []


class TodoSchema(BaseModel):
    id: int
    title: str
    is_important: Optional[bool] = False

    @classmethod
    def add_todo(cls, todo):
        if next(filter(lambda x: x.title == todo.title, TODOS), None) != None:
            return {'message': f"{todo.title} isimli ToDo mevcut"}
        else:
            TODOS.append(todo)
            return {'message': 'ToDo başarıyla eklendi'}

    @classmethod
    def remove_todo(cls, id):
        global TODOS
        TODOS = list(filter(lambda x: x.id != id, TODOS))
        return {'message': f'{id} ID\'ye sahip ToDo silindi'}

    @classmethod
    def get_todo_by_id(cls, id):
        todo = next(filter(lambda x: x.id == id, TODOS), None)
        return todo

    @classmethod
    def get_todos(cls):
        return TODOS

    @classmethod
    def update_todo(cls, todo):
        old_todo = next(filter(lambda x: x.id == todo.id, TODOS), None)
        if old_todo:
            old_todo = todo
            cls.remove_todo(old_todo.id)
            cls.add_todo(old_todo)
            return old_todo
        else:
            return {'message': 'ToDo bulunamadı!'}


app = FastAPI()


@app.get('/todos/')
async def get_todos():
    return {'todos': TodoSchema.get_todos()}


@app.post('/todos/')
async def add_todo(todo: TodoSchema):
    return TodoSchema.add_todo(todo)


@app.get('/todos/{id}/')
async def get_todo(id: int):
    return TodoSchema.get_todo_by_id(id)


@app.put('/todos/{id}/')
async def update_todo(id: int, todo: TodoSchema):
    return TodoSchema.update_todo(todo)


@app.delete('/todos/{id}/')
async def delete_todo(id: int):
    return TodoSchema.remove_todo(id)
