# BSD 3-Clause License
# Copyright (c) 2023, Yash-Sharma-1807


import psycopg2
from ..config import Config

DB_URI = Config.DB_URI
DB = psycopg2.connect(DB_URI)

cur = DB.cursor()

