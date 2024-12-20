from database.connection import get_db_connection

class Performance:
    """Performance model with CRUD operations."""
    def __init__(self, player_id, goals, assists, status, id=None):
        self.id = id
        self.player_id = player_id
        self.goals = goals
        self.assists = assists
        self.status = status

    def save(self):
        """Create or update the performance in the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        if self.id is None:
            # Create new performance
            query = "INSERT INTO performances (player_id, goals, assists, status) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (self.player_id, self.goals, self.assists, self.status))
            self.id = cursor.lastrowid
        else:
            # Update existing performance
            query = "UPDATE performances SET goals = ?, assists = ?, status = ? WHERE id = ?"
            cursor.execute(query, (self.goals, self.assists, self.status, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(performance_id):
        """Retrieve a performance by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, player_id, goals, assists, status FROM performances WHERE id = ?"
        cursor.execute(query, (performance_id,))
        row = cursor.fetchone()
        conn.close()
        return Performance(id=row[0], player_id=row[1], goals=row[2], assists=row[3], status=row[4]) if row else None

    @staticmethod
    def list_all():
        """List all performances."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT id, player_id, goals, assists, status FROM performances"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [
            Performance(id=row[0], player_id=row[1], goals=row[2], assists=row[3], status=row[4]) for row in rows
        ]

    @staticmethod
    def delete_by_id(performance_id):
        """Delete a performance by ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM performances WHERE id = ?"
        cursor.execute(query, (performance_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"Performance(id={self.id}, player_id={self.player_id}, goals={self.goals}, assists={self.assists}, status={self.status})"