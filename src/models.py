import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(50))
    firstname=Column(String(50))
    lastname=Column(String(50))
    email=Column(String(50))

class Post(Base):
    __tablename__='post'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)

class Comment(Base):
    __tablename__='comment'
    id=Column(Integer,primary_key=True)
    comment_text=Column(String(50))
    author_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    post_id=Column(Integer,ForeignKey('post.id'))
    post=relationship(Post)

class Media(Base):
    __tablename__='media'
    id=Column(Integer,primary_key=True)
    type=Column(Enum('image', 'video', name='media_type_enum'))
    url=Column(String(50))
    post_id=Column(Integer,ForeignKey('post.id'))
    post=relationship(Post)

class Follower(Base):
    __tablename__='follower'
    id=Column(Integer,primary_key=True)
    user_from_id=Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    user_to_id=Column(Integer,ForeignKey('user.id'))
    user_id=relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
