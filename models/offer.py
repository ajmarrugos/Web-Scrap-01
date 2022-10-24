#!/usr/bin/python3
"""This module contains the class Offer"""
import models
from os import getenv
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base
from hashlib import md5

class Offer(db.BaseModel):
    """This class is inherited from BaseModel used to create Offers"""
    __tablename__ = 'offers'
    tittle = Column(String(128), nullable=False)
    company = Column(String(128), nullable=False)
    location = Column(String(64), nullable=False)
    description = Column(String(256), nullable=False)
    salary = Column(Integer(32), nullable=False)
    currency = Column(String(16), nullable=False)

    def __init__(self, *args, **kwargs):
        """ initializes offer """
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
