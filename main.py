import schedule
import time
import conf_file
import calcul_hash
import compare_hash
import scan_ports

# Appeler la fonction ou exécuter le code nécessaire dans conf_file.py
conf_file.do()
calcul_hash.cal()
compare_hash.comp()
scan_ports.scanner_ports()


# Planifier l'exécution des fonctions
schedule.every(1).day.at("08:00").do(conf_file.do)  # Exécution quotidienne à 08:00
schedule.every().hour.do(calcul_hash.cal)  # Exécution toutes les heures
schedule.every(10).minutes.do(compare_hash.comp)  # Exécution toutes les 10 minutes
schedule.every().day.at("12:00").do(scan_ports.scanner_ports)  # Exécution quotidienne à 12:00

# Boucle d'exécution pour vérifier les tâches planifiées
while True:
    schedule.run_pending()
    time.sleep(1)