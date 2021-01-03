import sqlite3
from sqlite3 import Error


def create_connection(path):
	connection = None
	try:
		connection = sqlite3.connect(path)
		print("Connection to SQLite DB successful")
	except Error as e:
		print(f"The error '{e}' occurred")

	return connection


def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		print(connection.commit())
		print("Query executed successfully")
		return cursor.fetchall()
	except Error as e:
		print(f"The error '{e}' occurred")
		return e

def sqlString(string):
	return string.replace("'", "''")


connection = create_connection("whitelists.db")

execute_query(connection, """
CREATE TABLE IF NOT EXISTS WHITELIST(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id TEXT NOT NULL,
	minecraft_name TEXT NOT NULL
);
""")


def add_whitelist(id, name, is_sub, is_admin):
	if is_admin:
		execute_query(connection, f"""
			INSERT INTO WHITELIST(discord_id, minecraft_name)
			VALUES ('{id}', '{sqlString(name)}');
		""")
		return True
	elif is_sub and len(execute_query(connection, f"SELECT * FROM WHITELIST WHERE discord_id = '{id}'")) == 0:
		execute_query(connection, f"""
			INSERT INTO WHITELIST(discord_id, minecraft_name)
			VALUES ('{id}', '{sqlString(name)}');
		""")
		return True
	return False


def remove_whitelist(id, name, is_admin):
	if is_admin:
		execute_query(connection, f"""
		DELETE FROM WHITELIST
		WHERE minecraft_name = '{sqlString(name)}';""")
	else:
		if len(execute_query(connection, f"SELECT * FROM WHITELIST WHERE discord_id = '{id}' AND minecraft_name = '{name}'")) == 0:
			return False
		else:
			execute_query(connection, f"DELETE FROM WHITELIST WHERE discord_id = '{id}' AND minecraft_name = '{name}'")
			return True


