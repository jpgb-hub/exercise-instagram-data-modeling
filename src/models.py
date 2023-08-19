import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, backref
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    # Las relaciones con Post y Comment se establecerán desde las otras clases

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.ID'), primary_key=True)
    user_from = relationship("User", foreign_keys=[user_from_id], backref=backref("following", uselist=True))
    user_to = relationship("User", foreign_keys=[user_to_id], backref=backref("followed_by", uselist=True))

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship("Post", backref=backref("media", uselist=True))

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship("User", backref="posts")  # Relación con User

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship("Post", backref="comments")  # Relación con Post
    author = relationship("User", backref="comments")  # Relación con User
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e