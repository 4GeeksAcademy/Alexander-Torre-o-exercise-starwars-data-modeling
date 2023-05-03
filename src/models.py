import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, nullable=True)
    created_date = Column(DateTime, default=func.now())

class Favorites(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    description = Column(String(1000))
    diameter = Column(Integer, nullable=True)
    orbital_period = Column(String(2500), nullable=True)
    rotation_period = Column(Integer)
    terrain = Column(String(250))
    url = Column(String(250), unique=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(2500))
    mass = Column(String(250))
    gender = Column(String(250))
    url = Column(String(250), unique=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')