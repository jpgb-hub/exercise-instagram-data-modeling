import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)    
    

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_id=Column(Integer) 

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column (Integer)
    post_id = Column(Integer)

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
