from pydantic import BaseModel


class Todo(BaseModel):
    """Model for TODO app"""

    id: str
    title: str
    description: str
