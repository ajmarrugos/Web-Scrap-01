#!/usr/bin/python3
# Initialize the models package

from os import getenv
from models.engine.db import DBStorage

storage_t = getenv("HITCH_TYPE_STORAGE")
storage = DBStorage()
