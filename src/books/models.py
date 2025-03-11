from sqlmodel import SQLModel,Field,Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from src.db import models
import uuid
from datetime import datetime
from typing import Optional

class Book(SQLModel,table = True):
    __tablename__="books"
    
    uid:uuid.UUID = Field(
        sa_column= Column(
            pg.UUID,
            primary_key=True,
            nullable=False,
            default= uuid.uuid4
            
        )
    )
    title : str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language:str
    user_uid : Optional[uuid.UUID]= Field(default=None,foreign_key="users.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at:datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user : Optional["models.User"] = Relationship(back_populates="books")
    
    def __repr__(self) -> str:
        return f"<Book {self.title}>"