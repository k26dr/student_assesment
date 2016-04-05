import signal
import sys
import sqlite3
from flask import Flask, request, json

app = Flask(__name__)

# Create Database Table for attempts
conn = sqlite3.connect('server.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY, 
        student TEXT,
        assignment INTEGER,
        tests_passed INTEGER,
        tests_failed INTEGER
    );'''
)
conn.commit()
conn.close()

# Save attempt to database
@app.route('/attempt', methods=["POST"])
def save_attempt():
    conn = sqlite3.connect('server.db')
    c = conn.cursor()
    query = "INSERT INTO attempts (student, assignment, tests_passed, tests_failed) VALUES ('{0}', {1}, {2}, {3});".format(request.form['student'], request.form['assignment'], request.form['tests_passed'], request.form['tests_failed'])
    c.execute(query)
    conn.commit()
    conn.close()
    return json.jsonify(success=True)

# Display data for an assignment
@app.route('/assignment/<assignment_id>', methods=["GET"])
def assignment(assignment_id):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()
    query = "SELECT student, assignment, MAX(tests_passed) AS max_tests_passed, tests_failed FROM attempts WHERE assignment={0} GROUP BY student;".format(assignment_id)
    c.execute(query)
    result = []
    for tup in c.fetchall():
        result.append({"name": tup[0], "assignment": tup[1], "max_tests_passed": tup[2], "tests_failed": tup[3]})
    return json.jsonify(data=result)

if __name__ == '__main__':
    app.run(debug=True)
