from database.connection import get_db_connection

class Player:
    """Player model with CRUD operations."""
    def __init__(self, name, agent_id, id=None):
        self.id = id
        self.name = name
        self.agent_id = agent_id

    def save(self):
        """Create or update the player in the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            # Create new player
            query = "INSERT INTO players (name, agent_id) VALUES (?, ?)"
            cursor.execute(query, (self.name, self.agent_id))
            self.id = cursor.lastrowid
        else:
            # Update existing player
            query = "UPDATE players SET name = ?, agent_id = ? WHERE id = ?"
            cursor.execute(query, (self.name, self.agent_id, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(player_id):
        """Retrieve a player by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, name, agent_id FROM players WHERE id = ?"
        cursor.execute(query, (player_id,))
        row = cursor.fetchone()
        conn.close()
        return Player(id=row[0], name=row[1], agent_id=row[2]) if row else None

    @staticmethod
    def list_all():
        """List all players."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, name, agent_id FROM players"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [Player(id=row[0], name=row[1], agent_id=row[2]) for row in rows]

    @staticmethod
    def delete_by_id(player_id):
        """Delete a player by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM players WHERE id = ?"
        cursor.execute(query, (player_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"Player(id={self.id}, name={self.name}, agent_id={self.agent_id})"