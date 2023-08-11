from uuid import uuid4

from .db import todos
from .models import Todo


def generate_uuid():
    """Generate unique id with uuid4."""

    return str(uuid4())


async def todo_list() -> list[Todo]:
    """Return default todos list."""

    return todos


async def todo_create(todo: dict) -> Todo:
    """Create a new todo and append in the todos list."""

    new_todo = {
        "id": generate_uuid(),
        "title": todo["title"],
        "description": todo["description"],
    }
    todos.append(new_todo)
    return new_todo


async def todo_read(id: str) -> list[Todo]:
    """Get a single todo form the todo list using id."""

    todo = [todo for todo in todos if todo["id"] == id]
    return todo


async def todo_update(id: str, body: Todo) -> Todo:
    """Update a todo based on id."""

    todo = [todo for todo in todos if todo["id"] == id]
    todo = todo.update(body)
    return todo


async def todo_delete(id: str) -> str:
    """Delete a todo based on id."""

    todo = [todo for todo in todos if todo["id"] == id]
    if not todo:
        return f"No todo found based on the id: {id}"
    todos.remove(todo[0])
    return "Deleted"
