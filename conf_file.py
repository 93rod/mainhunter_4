import sqlite3
import time

def do():
    # Connexion à la base de données
    conn = sqlite3.connect('~/rootkit/hashes')
    cursor = conn.cursor()

    # Lecture du contenu du fichier conf
    with open('~/rootkit/rkh-conf', 'r') as file:
        lines = file.readlines()
        for line in lines:
            time.sleep(3)
            cursor.execute("INSERT INTO myhashes (path) VALUES (?)", (line.strip(),))
            conn.commit()
        
    conn.close()
