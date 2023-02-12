#!/usr/bin/python3
<<<<<<< HEAD
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


=======
"""Module for Filestorage autoinit."""

from models.engine.file_storage import FileStorage
>>>>>>> 64ea80399742e664f55679d408da6a558695dbae
storage = FileStorage()
storage.reload()
