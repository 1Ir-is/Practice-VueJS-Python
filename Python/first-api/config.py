import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "mysql+pymysql://root:techzen123@localhost:3306/mydb"
)

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int()