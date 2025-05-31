from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped , mapped_column
class Blog(Base):
    __tablename__ = "blogs"  
    id : Mapped[int]=mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()
#After Creating the Blog class in models.py import it into main.py and then create a database connection and then create a table in the database using the Base.metadata.create_all(engine) method.