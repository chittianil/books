from  sqlmodel import SQLModel,Column,Field
import  sqlalchemy.dialects.postgresql as pg
from typing import List
from src.books.schemas import Book
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    __tablename__ ='users'
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False,
            default=uuid.uuid4,
            # info={"description": "Unique identifier for the user account"},
        )
    )
    username: str
    first_name: str 
    last_name: str 
    role : str = Field(
        sa_column=Column(pg.VARCHAR,nullable=False, server_default="user")
    )
    is_verified: bool = Field(default=False)
    email :str 
    password_hash : str = Field(exclude=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    
    
    
    def __repr__(self):
        return f"User {self.username}"