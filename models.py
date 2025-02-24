from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#blog post model
class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = datetime.utcnow()

#comment model
class Comment(BaseModel):
    post_id: str
    text: str
    author: str
    created_at: Optional[datetime] = datetime.utcnow()
