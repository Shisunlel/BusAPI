from psycopg2 import connect
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
database = config['DATABASE'] if config else os.environ.get('DATABASE')
user = config['USER'] if config else os.environ.get('USER')
password = config['PASSWORD'] if config else os.environ.get('PASSWORD')
host = config['HOST'] if config else os.environ.get('HOST')

mydb = connect(database=database, user=user, password=password, host=host)
mycursor = mydb.cursor()
