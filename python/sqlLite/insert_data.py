from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    active: int

user1 = User(name="John", age="25", active=1)
user2 = User(name="Jane", age="30", active=1)
user3 = User(name="Mike", age="35", active=1)

engine = create_engine("sqlite:///users.db")

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()