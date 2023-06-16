import sqlite3
import time

def do():
    # Connexion à la base de données
    conn = sqlite3.connect('/home/lica/rootkit/hashes')
    cursor = conn.cursor()

    # Lecture du contenu du fichier conf
    with open('/home/lica/rootkit/rkh-conf', 'r') as file:
        lines = file.readlines()
        for line in lines:
            time.sleep(3)
            # Ajout de chaque ligne dans la colonne "path" de la base de données
            cursor.execute("INSERT INTO myhashes (path) VALUES (?)", (line.strip(),))
            conn.commit()
        
    # Fermeture de la connexion à la base de données
    conn.close()