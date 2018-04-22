
import sqlite3

conn = sqlite3.connect('test_db.sqlite3')
cursor = conn.cursor()

buffer = ""

while True:
    line = input()
    if line == "":
        continue
    buffer += line

    if sqlite3.complete_statement(buffer):
        buffer = buffer.strip()
        try:
            cursor = conn.execute(buffer)
            print(cursor.fetchall())

        except sqlite3.Error as e:
            print("An error occurred: ",e.args[0])
        finally:
            buffer = ""

conn.close()