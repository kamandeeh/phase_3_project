from database.connection import get_db_connection
import subprocess

DATABASE_URI = 'sqlite:///tables.db'

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    """Set up tables in the database."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            agent_id INTEGER NOT NULL,
            FOREIGN KEY (agent_id) REFERENCES agents (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            goals INTEGER NOT NULL,
            assists INTEGER NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (id)
        )
    """)
   
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
def setup():
    """Set up the database using Alembic migrations. Fallback to manual creation if needed."""
    try:
        # Run Alembic migrations
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Database setup complete using Alembic migrations.")
    except subprocess.CalledProcessError as e:
        print("Error running Alembic migrations:", e)
        print("Falling back to manual table creation...")
        create_tables()  
