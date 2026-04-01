from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Dummy login
USERNAME = "admin"
PASSWORD = "1234"

# Function to connect DB
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table (run once)
def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            status TEXT,
            priority TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials ❌"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    meetings = ["Sprint Meeting - 10 AM", "Client Call - 3 PM"]

    return render_template('dashboard.html', meetings=meetings, tasks=tasks)


# Add task route
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    status = request.form['status']
    priority = request.form['priority']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title, status, priority) VALUES (?, ?, ?)",
        (title, status, priority)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)