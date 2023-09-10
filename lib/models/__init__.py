import sqlite3

CONN = sqlite3.connect('task.db')
CURSOR = CONN.cursor()
