from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    content: str
    image_content: str
    creation_date: datetime
    starting_date: datetime
    completion_status: int

class TaskInput(BaseModel):
    title: str
    content: str
    image_content: str
    starting_date: datetime
    completion_status: int
