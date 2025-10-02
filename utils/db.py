import sqlite3
import pandas as pd
from datetime import datetime

def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS consultas
                 (id INTEGER PRIMARY KEY, fecha TEXT, nombre TEXT, edad TEXT, sintomas TEXT, resultado TEXT)''')
    conn.commit()
    conn.close()

def save_consulta(nombre, edad, sintomas, resultado):
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("INSERT INTO consultas (fecha, nombre, edad, sintomas, resultado) VALUES (?, ?, ?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M"), nombre, edad, sintomas, resultado))
    conn.commit()
    conn.close()

def get_historial():
    conn = sqlite3.connect("history.db")
    df = pd.read_sql_query("SELECT * FROM consultas ORDER BY id DESC", conn)
    conn.close()
    return df
