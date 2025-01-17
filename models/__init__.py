#!/usr/bin/python3
"""This module instantiates an object of either DBStorage or FileStorage based on the environment variable."""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Determine the storage type based on the environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE")

# Instantiate the appropriate storage class and reload its data
storage = DBStorage() if storage_type == "db" else FileStorage()
storage.reload()
