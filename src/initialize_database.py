from database_connection import get_database_connection

def drop_table(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE if exists player;")

def create_player_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE player
                   (name TEXT);""")
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_table(connection)
    create_player_table(connection)

if __name__ == "__main__":
    initialize_database()