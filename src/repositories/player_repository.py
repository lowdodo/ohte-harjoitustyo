from players.player import Player
from database_connection import get_database_connection
#reference from example todo-app 
"""
Repository for a single player to have one, chosen name.
"""
class PlayerRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
        self._player = None

    def name_the_player(self, name):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO player(name) VALUES (?)""" (name,))
        self._connection.commit()
        self._player = name
    
    def get_player_name(self):
        return self._player