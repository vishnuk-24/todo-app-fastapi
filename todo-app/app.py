from fastapi import FastAPI

from .models import Todo
from .todo import todo_create, todo_delete, todo_list, todo_read, todo_update

app = FastAPI()


@app.get("/")
async def get_todo() -> list[dict]:
    """Return list of todo tasks."""
    return await todo_list()


@app.post("/")
async def create_todo(todo: dict) -> Todo:
    """Create a todo."""
    return await todo_create(todo)


@app.get("/{id}")
async def get_todo(id: str) -> list[Todo]:
    """Get todo based on id."""
    return await todo_read(id)


@app.put("/{id}")
async def put_todo(id: str, body: Todo) -> Todo:
    """Update todo."""
    return await todo_update(id, body)


@app.delete("/{id}")
async def delete_todo(id: str) -> list:
    """Delete todo."""
    return await todo_delete(id)
