import psycopg2

from flask import Flask

app = Flask(__name__)

database = "postgresql://my_flask_db_wgpw_user:vcERD0bJXHzhiBnx02k6vccFsdqdNRY3@dpg-cqi188iju9rs73ca39sg-a/my_flask_db_wgpw"

@app.route('/')
def hello_world():
    return 'Hello, World from Eric Pihlstrom in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(database)
    conn.close()
    return "Database connection successful!"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    conn.close()
    response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for row in records:
        response += "<tr>"
        for item in row:
            response += f"<td>{item}</td>"
        response += "</tr>"
    response += "</table>"
    return response

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(database)
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    conn.close()
    return "Basketball table dropped"
