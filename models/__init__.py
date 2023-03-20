#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
if environ['HBNB_TYPE_STORAGE'] == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
