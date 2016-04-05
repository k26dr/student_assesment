import signal
import sys
import sqlite3
from contextlib import contextmanager
from flask import Flask, request, json
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

def run_query(query):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

@contextmanager
def run_query_context(query):
    conn = sqlite3.connect('server.db')
    c = conn.cursor()
    c.execute(query)
    yield c
    conn.close()
    
# Create Database Table for attempts
run_query('''
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY, 
        student TEXT,
        assignment INTEGER,
        tests_passed INTEGER,
        tests_failed INTEGER
    );'''
)

# Save attempt to database
@app.route('/attempt', methods=["POST"])
def save_attempt():
    query = """INSERT INTO attempts (student, assignment, tests_passed, tests_failed) 
        VALUES ('{0}', {1}, {2}, {3});
        """.format(request.form['student'], request.form['assignment'], 
            request.form['tests_passed'], request.form['tests_failed'])
    run_query(query)
    return json.jsonify(success=True)

# Display data for an assignment
@app.route('/assignment/<assignment_id>', methods=["GET"])
def assignment(assignment_id):
    query = """SELECT student, assignment, MAX(tests_passed) AS max_tests_passed, tests_failed 
        FROM attempts WHERE assignment={0} 
        GROUP BY student;
        """.format(assignment_id)
    result = []
    with run_query_context(query) as c:
        for tup in c.fetchall():
            result.append({ "name": tup[0], "assignment": tup[1], 
                "max_tests_passed": tup[2], "tests_failed": tup[3] })
    return json.jsonify(data=result)

if __name__ == '__main__':
    app.run(debug=True)
