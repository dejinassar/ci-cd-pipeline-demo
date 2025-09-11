from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory DB
todos = []

@app.get("/")
def root():
    return {"message": "CI/CD Pipeline Demo App Running"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return {"msg": "Todo added", "todo": todo}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for t in todos:
        if t["id"] == todo_id:
            t.update(todo.dict())
            return {"msg": "Todo updated", "todo": t}
    return {"msg": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"msg": "Todo deleted"}
