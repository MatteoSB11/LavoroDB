from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Abilita CORS su tutte le route

# Configurazione connessione al database
DB_CONFIG = {
    'host': 'localhost',
    'user': 'pythonuser',      # Sostituisci se necessario
    'password': 'password123', # Sostituisci se necessario
    'database': 'dambarra'
}

def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

@app.route('/players', methods=['GET'])
def get_players():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM players')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')