import sqlite3
from flask import Flask, render_template, request 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add.html", methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        content = request.form['addNote']
        conn = get_db_connection()
        conn.execute("INSERT INTO entries (content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
        return render_template('add.html')
    else:
        return render_template('add.html')

@app.route("/index.html")
def indexLink():
    return render_template('index.html')

@app.route("/get.html")
def get():
    conn = get_db_connection()
    #entry = conn.execute('SELECT * FROM entries WHERE id IN (SELECT id FROM entries ORDER BY RANDOM() LIMIT 1)').fetchone()
    #entry = 'hey'
    entry = conn.execute('SELECT * FROM entries ORDER BY random() LIMIT 1').fetchall()
    conn.close()
    return render_template('get.html', entry=entry)

app.run(host="localhost", port="8080", debug=True)