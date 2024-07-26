import psycopg2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Eric Pihlstrom in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://my_flask_db_wgpw_user:vcERD0bJXHzhiBnx02k6vccFsdqdNRY3@dpg-cqi188iju9rs73ca39sg-a/my_flask_db_wgpw")
    conn.close()
    return "Database connection successful!"
