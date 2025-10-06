import mysql.connector
import csv

# Configura la connessione al database
conn = mysql.connector.connect(
    host='localhost',
    user='pythonuser',      # Sostituisci con il tuo utente MariaDB
    password='password123',# Sostituisci con la tua password
    database='dambarra' # Sostituisci con il tuo database
)
cur = conn.cursor()

# Crea la tabella se non esiste
cur.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INT PRIMARY KEY,
    player VARCHAR(100),
    team VARCHAR(100),
    goals INT
)
''')

# Leggi il CSV e importa i dati
with open('players.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute('''
            REPLACE INTO players (id, player, team, goals)
            VALUES (%s, %s, %s, %s)
        ''', (row['id'], row['player'], row['team'], row['goals']))

conn.commit()
cur.close()
conn.close()