import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def database_connect():
    conn = psycopg2.connect(
        host = "db-hw3.crdbanw3f7pw.us-east-2.rds.amazonaws.com",
        database = "postgres",
        user = "postgres",
        password = "Musoke0606"
    )
    return conn


@app.route("/")
def database_version():
    conn = database_connect()
    cur = conn.cursor()

    cur.execute('SELECT VERSION();')
    database_version = curr.fetchall()

    cur.close()
    conn.close()

    return render_template('index.html', database_version= database_version)
