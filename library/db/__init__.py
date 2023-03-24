import psycopg2
from library.db.config import config
conn = psycopg2.connect(**config)