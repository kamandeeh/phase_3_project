from database.connection import get_db_connection

class Agent:
    """Agent model with CRUD operations."""
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        """Create or update the agent in the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            # Create new agent
            query = "INSERT INTO agents (name) VALUES (?)"
            cursor.execute(query, (self.name,))
            self.id = cursor.lastrowid
        else:
            # Update existing agent
            query = "UPDATE agents SET name = ? WHERE id = ?"
            cursor.execute(query, (self.name, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(agent_id):
        """Retrieve an agent by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, name FROM agents WHERE id = ?"
        cursor.execute(query, (agent_id,))
        row = cursor.fetchone()
        conn.close()
        return Agent(id=row[0], name=row[1]) if row else None

    @staticmethod
    def list_all():
        """List all agents."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, name FROM agents"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [Agent(id=row[0], name=row[1]) for row in rows]

    @staticmethod
    def delete_by_id(agent_id):
        """Delete an agent by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM agents WHERE id = ?"
        cursor.execute(query, (agent_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"Agent(id={self.id}, name={self.name})"