import sqlite3
from flask import Flask

app = Flask(__name__)
conn = sqlite3.connect('server.db')

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS foo (
        id INTEGER PRIMARY KEY, 
        student TEXT,
        assignment INTEGER,
        tests_passed INTEGER,
        tests_failed INTEGER
    );'''
)
conn.commit()

@app.route('/attempt', methods: ["GET"])
def 

if __name__ == '__main__':
    app.run()
