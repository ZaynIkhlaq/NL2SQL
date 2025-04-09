import sqlite3
import requests
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from langchain_community.utilities.sql_database import SQLDatabase

# Set up engine for in-memory database access
def get_engine_for_chinook_db():
    """Pull sql file, populate in-memory database, and create engine."""
    url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sql"
    response = requests.get(url)
    sql_script = response.text

    connection = sqlite3.connect(":memory:", check_same_thread=False)
    connection.executescript(sql_script)
    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )

engine = get_engine_for_chinook_db()
db = SQLDatabase(engine)

def test_database_connection():
    try:
        # Example query to test the connection
        result = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = result.fetchall()
        print("Tables in the database:", tables)
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False

# Run the test
if test_database_connection():
    print("Database engine is working and accessible.")
else:
    print("There was an issue with the database engine.")
