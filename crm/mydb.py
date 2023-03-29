from mysql import connector

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)


# Cursor
cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE dataset1") 